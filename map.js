// map.js
// Логика и инициализация окон карт

let googleMap = null; // карта одна на весь сайт
let mapMarkers = [];
let currentInfoWindow = null;
let lastDayIdWithMap = null; // чтобы не пересоздавать карту если не надо

function onGoogleMapsReady() {
  window.showDayOnMap = function(day) {
    if (!day) return;
    const mapDiv = document.getElementById(`map-day-${day.id}`);
    if (!mapDiv) return;
    mapDiv.style.opacity = 0;
    setTimeout(() => {
      let center = { lat: 35.68096, lng: 139.76735 };
      const firstLoc = day.timeline.find(ev => ev.location && ev.location.lat && ev.location.lng);
      if (firstLoc) center = { lat: firstLoc.location.lat, lng: firstLoc.location.lng };

      // инициализация карты или update
      if (!googleMap || lastDayIdWithMap !== day.id) {
        googleMap = new google.maps.Map(mapDiv, {
          center: center,
          zoom: 12,
          mapTypeControl: false,
          streetViewControl: false,
        });
      } else {
        googleMap.setCenter(center);
        googleMap.setZoom(12);
      }
      lastDayIdWithMap = day.id;

      if (mapMarkers.length) mapMarkers.forEach(m => m?.marker?.setMap(null));
      mapMarkers = [];
      day.timeline.forEach((ev, idx) => {
        if (ev.location && ev.location.lat && ev.location.lng) {
          const marker = new google.maps.Marker({
            position: {lat: ev.location.lat, lng: ev.location.lng},
            map: googleMap,
            title: ev.title
          });
          const infoContent = `<div><b>${ev.title}</b><br>${ev.time}<br><a href='${ev.location.mapsUrl}' target='_blank'>Открыть в Google Maps</a></div>`;
          const infowindow = new google.maps.InfoWindow({content: infoContent});
          marker.addListener('click', () => {
            if (currentInfoWindow) currentInfoWindow.close();
            infowindow.open({ anchor: marker, map: googleMap, shouldFocus: false });
            currentInfoWindow = infowindow;
          });
          mapMarkers.push({marker, infowindow});
        } else {
          mapMarkers.push(null);
        }
      });
      // fade in карта
      mapDiv.style.opacity = 1;
      // для клика по таймлайну экспортируем
      window._map_focusEventOnMap = function(idx) {
        const markerObj = mapMarkers[idx];
        if (markerObj && markerObj.marker && markerObj.infowindow) {
          googleMap.panTo(markerObj.marker.getPosition());
          googleMap.setZoom(15);
          if (currentInfoWindow) currentInfoWindow.close();
          markerObj.infowindow.open({ anchor: markerObj.marker, map: googleMap, shouldFocus: false });
          currentInfoWindow = markerObj.infowindow;
        }
      };
    }, 50);
  };
}
