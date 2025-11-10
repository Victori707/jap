<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Путешествие в Японию</title>
  <style>
body {
  font-family: 'Roboto', 'Open Sans', Arial, sans-serif;
  background: #191620;
  margin: 0;
  color: #fff;
}
header {
  background: #ff3399;
  color: #fff;
  padding: 20px;
  text-align: center;
}
.dates {
  font-size: 1.2em;
  color: #feaad6;
}
main {
  max-width: 1100px;
  margin: 20px auto 40px auto;
  padding: 20px;
  background: #101010;
  border-radius: 14px;
  box-shadow: 0 4px 24px rgba(255,51,153,0.11);
}
.day-navigation {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 10px 0 15px 0;
  position: sticky;
  top: 0;
  background: #101010;
  z-index: 10;
  border-bottom: 3px solid #ff3399;
}
.day-nav-btn.active {
  background: linear-gradient(90deg,#ff3399 70%,#fe52c0 100%);
  color: #fff !important;
  border: none;
  outline: none;
  font-weight: bold;
  box-shadow: 0 2px 12px rgba(254,82,192,0.16);
  transition: background 0.2s;
}
.day-nav-btn {
  background: #101010;
  color: #ff3399;
  border: 2px solid #ff3399;
  border-radius: 7px;
  padding: 7px 13px;
  font-size: 1.06em;
  cursor: pointer;
  font-weight: bold;
  letter-spacing:1px;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s;
}
.day-nav-btn:not(.active):hover {
  background: #2b2430;
  color: #fff;
  box-shadow: 0 0 14px #ff339995;
  border-color:#fe52c0;
}
footer {
  text-align: center;
  color: #feaad6;
  font-size: 0.98em;
  padding-bottom: 24px;
}
.day {
  margin-bottom: 45px;
  border-bottom: 1px solid #332537;
  padding-bottom: 36px;
}
.day-notes {
  margin-bottom: 6px;
  color: #fe52c0;
  font-size: 1.08em;
}
.day-summary {
  margin-bottom: 18px;
  color: #ffb2ec;
}
.day-content {
  display: flex;
  gap: 28px;
  align-items: flex-start;
}
.timeline-col {
  flex: 2;
  min-width: 210px;
}
.timeline-list {
  list-style: none;
  padding: 0;
  margin: 0;
  border-left: 4px solid #fe52c0;
  position: relative;
}
.timeline-event {
  position: relative;
  margin-bottom: 35px;
  padding-left: 34px;
  min-height: 36px;
  color: #fff;
  background: transparent;
  transition: background 0.22s;
  cursor: pointer;
  user-select: none;
}
.timeline-event::before {
  content: '';
  position: absolute;
  left: -11px;
  top: 7px;
  width: 18px;
  height: 18px;
  background: radial-gradient(circle,#fff 0%,#ff3399 40%); 
  border: 4px solid #fe52c0;
  box-shadow: 0 0 12px #ff3399a8, 0 2px 8px #10101044;
  border-radius: 50%;
  z-index: 1;
}
.timeline-event:hover, .timeline-event.selected {
  background: #2b1b24;
  box-shadow: 0 4px 14px #fe52c0 44, 0 1.5px 8px #10101066;
  border-left: 4.5px solid #ff3399;
  outline:1.3px solid #fe52c0aa;
  color: #ffb2ec;
}
.timeline-event time {
  font-size: 0.97em;
  color: #feaad6;
  font-weight: bold;
  margin-right: 8px;
}
.ev-note {
  margin-top: 3px;
  color: #feaad6;
  font-size: 0.97em;
}
.map-col {
  flex: 3;
  min-width: 260px;
}
.map-container {
  width: 100%;
  min-height: 220px;
  background: linear-gradient(120deg,#251c28,#32232b,#20111f 84%);
  border: 2px solid #ff339958;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #b751a7;
  font-size: 1.1em;
  margin-bottom:8px;
  opacity: 0;
  animation: fadeInMap 0.7s forwards;
  box-shadow:0 2px 13px #ff339944;
}
@keyframes fadeInMap {
  0% { opacity: 0; }
  70% { opacity: 0.4; }
  100% { opacity: 1; }
}
@media (max-width: 800px) {
  main {
    padding: 5px;
  }
  .day-content {
    flex-direction: column;
  }
  .timeline-col, .map-col {
    min-width: 180px;
    width: 100%;
  }
  .map-container {
    min-height: 165px;
  }
}
#devmode-bar {
  width: 100vw;
  background: #222026;
  padding: 8px 0 4px 0;
  text-align: right;
  z-index: 100;
}
#devmode-toggle {
  font-weight: bold;
  font-size:1.04em;
  padding: 6px 16px;
  border-radius: 7px;
  border: 2px solid #ff3399;
  margin: 0 14px;
  background: #18121e;
  color: #ff3399;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, border 0.18s;
}
#devmode-toggle.dev {
  background: #ff3399;
  color: #fff;
  box-shadow: 0 2px 14px #ff339956;
  border:2px solid #fff!important;
}
#devmode-toggle:hover {
  background: #332031;
  color: #fff;
}
body.devmode [contenteditable="true"] {
  outline: 2px dashed #fe52c0;
  background: #23172a;
  border-radius: 6px;
  cursor: text;
  box-shadow: 0 0 5px #fe52c096;
  transition: outline 0.13s;
}
body.devmode .editable-input {
  border: 2px dashed #ff3399;
  padding: 2px 7px;
  border-radius: 7px;
  background: #232;
  color: #ffb2ec;
  font-size: 1em;
  margin-bottom: 4px;
}
body.devmode select.editable-input {
  background: #2b1c29;
  color: #ff3399;
  border-color: #fe52c0;
  cursor: pointer;
}
body.devmode select.editable-input option {
  background: #101010;
  color: #ffb2ec;
}
body.devmode .photo-upload {
  display: block;
  background: #2b1c29;
  border:1.5px solid #ff339988;
  color:#ff3399;
  margin: 7px 0 0 0;
  border-radius:8px;
  padding:6px;
  font-size: 0.99em;
  transition:background 0.15s;
}
body.devmode .photo-upload:hover {
  background: #31202a;
}
.uploaded-photo {
  max-width: 95%;
  margin: 10px 0 0 0;
  border-radius: 13px;
  border:2px solid #ff339955;
  box-shadow:0 0 12px #fe52c051;
}
.dev-photo-delete {
  color: #fff;
  background: #ff3399;
  border:none;
  padding: 4px 14px;
  border-radius:6px;
  cursor:pointer;
  font-size:0.97em;
  margin: 6px 0 0 9px;
  transition:background 0.13s;
}
.dev-photo-delete:hover {
  background: #2b1c29;
  color:#ff3399;
  border:1.5px solid #ff3399;
}
#computed-total {
  font-weight: bold;
  color: #ff3399;
  font-size: 1.1em;
}
.pulse {
  animation: pulse 0.5s ease-in-out;
}
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); color: #fe52c0; }
}
  </style>
</head>
<body>
  <div id="devmode-bar">
    <button id="devmode-toggle" onclick="toggleDevMode()">Войти в режим разработчика</button>
  </div>
  <header>
    <h1 contenteditable="false">Путешествие в Японию</h1>
    <p class="dates"><span id="trip-dates"></span></p>
  </header>
  <main>
    <nav id="day-nav" class="day-navigation"></nav>
    <section id="itinerary"></section>
  </main>
  <footer>
    <div>Создатель: <span id="author-name">Ваше Имя</span>.</div>
    <div>Общий бюджет: <span id="budget"></span></div>
    <div style="margin-top: 10px;">Подсчёт по дням: <span id="computed-total">Загрузка...</span></div>
  </footer>
  <script>
    // Встроенные данные - загружаются из localStorage или используются дефолтные
    window.embeddedData = {
      "dates": "16–29 ноября 2025",
      "budget": "~180 000 ₽",
      "author": "Ваше Имя",
      "header": "Путешествие в Японию",
      "days": []
    };
  </script>
  <script>
// script.js - полностью встроен

let daysData = [];
let tripDataRaw = null;
let isDevMode = false;
const RATE_JPY_TO_RUB = 0.68;

function formatRub(n) {
  const num = Number(n || 0);
  return num.toLocaleString('ru-RU');
}
function coerceExpense(v) {
  if (typeof v === 'number') return v;
  if (!v) return 0;
  const digits = String(v).replace(/[^0-9]/g, '');
  return digits ? Number(digits) : 0;
}

function loadData() {
  if (window.embeddedData) {
    return Promise.resolve(window.embeddedData);
  }
  const ls = localStorage.getItem('jp_itin_v1');
  if (ls) return Promise.resolve(JSON.parse(ls));
  return Promise.resolve({
    "dates": "16–29 ноября 2025",
    "budget": "~180 000 ₽",
    "author": "Ваше Имя",
    "header": "Путешествие в Японию",
    "days": []
  });
}

function saveData(data) {
  localStorage.setItem('jp_itin_v1', JSON.stringify(data));
}

function computeAndRenderTotals() {
  if (!daysData || daysData.length === 0) {
    document.getElementById('computed-total').textContent = '0 ₽';
    return;
  }
  let totalRUB = 0;
  let totalJPY = 0;
  daysData.forEach(day => {
    const exp = coerceExpense(day.expenses);
    const currency = day.currency || 'RUB';
    if (currency === 'JPY') {
      totalJPY += exp;
    } else {
      totalRUB += exp;
    }
  });
  const jpyInRub = totalJPY * RATE_JPY_TO_RUB;
  const grandTotal = totalRUB + jpyInRub;
  const totalEl = document.getElementById('computed-total');
  if (totalEl) {
    let text = `${formatRub(Math.round(grandTotal))} ₽`;
    if (totalJPY > 0) {
      text += ` (${formatRub(totalJPY)} ¥ = ${formatRub(Math.round(jpyInRub))} ₽ по курсу ${RATE_JPY_TO_RUB} + ${formatRub(totalRUB)} ₽)`;
    }
    totalEl.textContent = text;
    totalEl.classList.add('pulse');
    setTimeout(() => totalEl.classList.remove('pulse'), 500);
  }
}

function setDevMode(state) {
  isDevMode = !!state;
  document.body.classList.toggle('devmode', isDevMode);
  const btn = document.getElementById('devmode-toggle');
  if (btn) {
    btn.classList.toggle('dev', isDevMode);
    btn.textContent = isDevMode ? 'Выйти из режима разработчика' : 'Войти в режим разработчика';
  }
  const devBar = document.getElementById('devmode-bar');
  if (devBar) {
    let saveBtn = document.getElementById('save-plan-btn');
    let saveHtmlBtn = document.getElementById('save-html-btn');
    if (isDevMode) {
      if (!saveBtn) {
        saveBtn = document.createElement('button');
        saveBtn.id = 'save-plan-btn';
        saveBtn.textContent = '📝 Сохранить план';
        saveBtn.style.cssText = 'margin-left: 10px; padding: 8px 16px; background: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 14px;';
        saveBtn.onclick = savePlanToServer;
        devBar.appendChild(saveBtn);
      }
      if (!saveHtmlBtn) {
        saveHtmlBtn = document.createElement('button');
        saveHtmlBtn.id = 'save-html-btn';
        saveHtmlBtn.textContent = '💾 Сохранить HTML';
        saveHtmlBtn.style.cssText = 'margin-left: 10px; padding: 8px 16px; background: #2196F3; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 14px;';
        saveHtmlBtn.onclick = saveHTMLToFile;
        devBar.appendChild(saveHtmlBtn);
      }
    } else {
      if (saveBtn) saveBtn.remove();
      if (saveHtmlBtn) saveHtmlBtn.remove();
    }
  }
  renderTripInfo(tripDataRaw);
  renderDayNavigation(daysData);
  renderItinerary(daysData);
}

function toggleDevMode() {
  setDevMode(!isDevMode);
  localStorage.setItem('jp_itin_devmode', isDevMode ? '1':'');
}

async function savePlanToServer() {
  try {
    const response = await fetch('/data/itinerary.json', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(tripDataRaw)
    });
    if (response.ok) {
      alert('✅ План сохранён на сервере!');
    } else {
      alert('⚠️ Сервер недоступен. Данные сохранены локально.');
    }
  } catch (e) {
    alert('⚠️ Сервер недоступен. Данные сохранены локально.');
  }
}

async function saveHTMLToFile() {
  try {
    const htmlContent = document.documentElement.outerHTML;
    const blob = new Blob([htmlContent], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'index_saved.html';
    a.click();
    URL.revokeObjectURL(url);
    alert('✅ HTML файл скачан!');
  } catch (error) {
    alert('❌ Ошибка: ' + error.message);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  isDevMode = !!localStorage.getItem('jp_itin_devmode');
  loadData().then(data => {
    tripDataRaw = data;
    tripDataRaw.days = (tripDataRaw.days || []).map(d => ({
      ...d,
      expenses: coerceExpense(d.expenses)
    }));
    daysData = tripDataRaw.days;
    setDevMode(isDevMode);
    computeAndRenderTotals();
  });
});

function renderTripInfo(data) {
  const dates = document.getElementById('trip-dates');
  const budget = document.getElementById('budget');
  const author = document.getElementById('author-name');
  const header = document.querySelector('header h1');
  if (dates) dates.textContent = data.dates || '';
  if (budget) budget.textContent = data.budget || '';
  if (author) {
    author.textContent = data.author || 'Ваше Имя';
    author.contentEditable = isDevMode;
    author.oninput = () => { tripDataRaw.author = author.textContent; saveData(tripDataRaw); };
  }
  if (header) {
    header.contentEditable = isDevMode;
    header.oninput = () => { tripDataRaw.header = header.textContent; saveData(tripDataRaw); };
    if (tripDataRaw.header) header.textContent = tripDataRaw.header;
  }
  if (isDevMode) {
    if (dates) {
      dates.contentEditable = true;
      dates.oninput = () => { tripDataRaw.dates = dates.textContent; saveData(tripDataRaw); };
    }
    if (budget) {
      budget.contentEditable = true;
      budget.oninput = () => { tripDataRaw.budget = budget.textContent; saveData(tripDataRaw); };
    }
  } else {
    if (dates) dates.contentEditable = false;
    if (budget) budget.contentEditable = false;
  }
}

function renderDayNavigation(days) {
  const nav = document.getElementById('day-nav');
  if (!nav) return;
  nav.innerHTML = '';
  days.forEach((day, idx) => {
    const btn = document.createElement('button');
    btn.textContent = `День ${idx + 1}`;
    btn.className = 'day-nav-btn';
    btn.dataset.dayIdx = idx;
    btn.onclick = () => {
      setActiveDay(idx);
      scrollToDay(day.id);
    };
    nav.appendChild(btn);
  });
  if (days.length > 0) setActiveDay(0);
}

function setActiveDay(idx, skipMap) {
  const nav = document.getElementById('day-nav');
  if (!nav) return;
  const buttons = nav.querySelectorAll('button');
  buttons.forEach(b => b.classList.remove('active'));
  if (buttons[idx]) buttons[idx].classList.add('active');
}

window.addEventListener('scroll', () => {
  const daySections = Array.from(document.querySelectorAll('.day'));
  if (daySections.length === 0) return;
  let minDiff = Infinity, idxToActivate = 0;
  const scrollY = window.scrollY + 70;
  daySections.forEach((sec, i) => {
    const diff = Math.abs(sec.offsetTop - scrollY);
    if (diff < minDiff) {
      minDiff = diff;
      idxToActivate = i;
    }
  });
  setActiveDay(idxToActivate, true);
});

window.focusEventOnMap = function(idx) {
  const timelineEvents = document.querySelectorAll('.timeline-list .timeline-event');
  timelineEvents.forEach(ev => ev.classList.remove('selected'));
  if (timelineEvents[idx]) {
    timelineEvents[idx].classList.add('selected');
    if (window.innerWidth < 800) {
      const section = timelineEvents[idx].closest('.day');
      if (section) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
}

function scrollToDay(dayId) {
  const section = document.getElementById(`day-${dayId}`);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

function renderItinerary(days) {
  const root = document.getElementById('itinerary');
  if (!root) return;
  root.innerHTML = '';
  days.forEach((day, idx) => {
    const daySection = document.createElement('section');
    daySection.className = 'day';
    daySection.id = `day-${day.id}`;
    daySection.setAttribute('data-day-idx', idx);

    const titleBlock = isDevMode
      ? `<div class="day-notes" contenteditable="true" data-df="title" data-day-idx="${idx}">${day.title||''}</div>`
      : `<div class="day-notes"><strong>${day.title||''}</strong></div>`;
    const notesBlock = isDevMode
      ? `<div class="dev-daynotes" contenteditable="true" data-df="notes" data-day-idx="${idx}">${day.notes||''}</div>`
      : `<div class="dev-daynotes">${day.notes||''}</div>`;

    const expVal = coerceExpense(day.expenses);
    const currency = day.currency || 'RUB';
    const currencySymbol = currency === 'JPY' ? '¥' : '₽';
    const jpyEquivalent = currency === 'JPY' ? ` (~${formatRub(Math.round(expVal * RATE_JPY_TO_RUB))} ₽ по курсу ${RATE_JPY_TO_RUB})` : '';
    
    const expensesBlock = isDevMode
      ? `<div class="day-summary">Итоговые траты: <input class="editable-input" type="number" min="0" step="100" value="${expVal}" data-expenses="${idx}" /> <select class="editable-input" data-currency="${idx}" style="width:80px;margin-left:4px;">
          <option value="RUB" ${currency === 'RUB' ? 'selected' : ''}>₽ (руб)</option>
          <option value="JPY" ${currency === 'JPY' ? 'selected' : ''}>¥ (иены)</option>
        </select></div>`
      : `<div class="day-summary">Итоговые траты: <b>${formatRub(expVal)} ${currencySymbol}${jpyEquivalent}</b></div>`;

    let mediaBlock = '';
    if (isDevMode) {
      mediaBlock = `<input type="file" accept="image/*" class="photo-upload" data-day="${day.id}" data-day-idx="${idx}" />`+(day.photo ? `<img src="${day.photo}" class="uploaded-photo"><button class="dev-photo-delete" data-day="${day.id}" data-day-idx="${idx}">Удалить фото</button>`:'');
    } else if (day.photo) {
      mediaBlock = `<img src="${day.photo}" alt="photo" class="uploaded-photo">`;
    }

    let timelineHtml = '';
    day.timeline.forEach((ev, eidx) => {
      if (!isDevMode) {
        const mapsUrl = ev.location && ev.location.mapsUrl ? ev.location.mapsUrl : null;
        const handlerStr = mapsUrl ?
          `event.stopPropagation(); if(window._tlClickHandler) window._tlClickHandler(${eidx}, '${mapsUrl.replace(/'/g, "\\'")}');` :
          `event.stopPropagation(); if(window._tlClickHandler) window._tlClickHandler(${eidx}, null);`;
        timelineHtml += `
<li class="timeline-event" onclick="${handlerStr}">
  <time>${ev.time||''}</time> ${ev.title||''}
  <div class="ev-note">${ev.note || ''}</div>
</li>`;
      } else {
        timelineHtml += `
<li class="timeline-event editing" data-eidx="${eidx}" data-day-idx="${idx}">
  <input class="editable-input" type="text" value="${ev.time||''}" data-ef="time" size="6" placeholder="Время">
  <input class="editable-input" type="text" value="${ev.title||''}" data-ef="title" size="18" placeholder="Название">
  <input class="editable-input" type="text" value="${(ev.location&&ev.location.mapsUrl)||''}" data-ef="mapsUrl" size="28" placeholder="Google Maps URL (опц.)">
  <input class="editable-input" type="text" value="${ev.note||''}" data-ef="note" size="28" placeholder="Примечание">
  <button class="dev-photo-delete" data-del-evt="${eidx}" data-day-idx="${idx}">–</button>
</li>`;
      }
    });
    if (isDevMode) {
      timelineHtml += `<button class="photo-upload" data-add-evt="${day.id}" data-day-idx="${idx}">+ Добавить событие</button>`;
    }

    daySection.innerHTML = `
      <h2 contenteditable="${isDevMode}" data-df="date" data-day-idx="${idx}">День ${idx+1}: ${day.date||''}</h2>
      ${titleBlock}
      ${notesBlock}
      ${expensesBlock}
      <div class="day-content">
        <div class="timeline-col">
          <ul class="timeline-list">${timelineHtml}</ul>
        </div>
        ${mediaBlock ? `<div class="map-col">${mediaBlock}</div>` : ''}
      </div>
    `;
    root.appendChild(daySection);
  });
  if (isDevMode) addDevmodeHandlers();
  else window._tlClickHandler = (idx, url) => { 
    if (window.focusEventOnMap) window.focusEventOnMap(idx); 
    if(url) window.open(url,'_blank'); 
  };
  computeAndRenderTotals();
}

function addDevmodeHandlers() {
  document.querySelectorAll('[contenteditable][data-df][data-day-idx]').forEach(el => {
    const dayIdx = Number(el.getAttribute('data-day-idx'));
    if (isNaN(dayIdx) || dayIdx < 0 || dayIdx >= daysData.length) return;
    el.oninput = () => {
      const key = el.getAttribute('data-df');
      const val = el.innerText.trim();
      if (key === 'date') {
        daysData[dayIdx].date = val.replace(/^День\s+\d+:\s*/i,'');
      } else {
        daysData[dayIdx][key] = val;
      }
      saveData(tripDataRaw);
      computeAndRenderTotals();
    };
  });
  
  document.querySelectorAll('input[data-expenses]').forEach(inp => {
    const idx = Number(inp.getAttribute('data-expenses'));
    if (isNaN(idx) || idx < 0 || idx >= daysData.length) return;
    inp.oninput = () => {
      daysData[idx].expenses = coerceExpense(inp.value);
      saveData(tripDataRaw);
      computeAndRenderTotals();
    };
  });
  
  document.querySelectorAll('select[data-currency]').forEach(sel => {
    const idx = Number(sel.getAttribute('data-currency'));
    if (isNaN(idx) || idx < 0 || idx >= daysData.length) return;
    sel.onchange = () => {
      daysData[idx].currency = sel.value;
      saveData(tripDataRaw);
      renderItinerary(daysData);
      computeAndRenderTotals();
    };
  });
  
  document.querySelectorAll('.timeline-event.editing[data-day-idx]').forEach((li) => {
    const dayIdx = Number(li.getAttribute('data-day-idx'));
    const eidx = Number(li.getAttribute('data-eidx'));
    if (isNaN(dayIdx) || dayIdx < 0 || dayIdx >= daysData.length) return;
    if (isNaN(eidx) || eidx < 0 || eidx >= (daysData[dayIdx].timeline || []).length) return;
    
    ['time','title','mapsUrl','note'].forEach(field => {
      const inp = li.querySelector(`[data-ef="${field}"]`);
      if (!inp) return;
      inp.oninput = () => {
        const val = inp.value;
        if (field === 'mapsUrl') {
          if (!daysData[dayIdx].timeline[eidx].location) daysData[dayIdx].timeline[eidx].location = {};
          daysData[dayIdx].timeline[eidx].location.mapsUrl = val;
        } else {
          daysData[dayIdx].timeline[eidx][field] = val;
        }
        saveData(tripDataRaw);
      };
    });
    
    const del = li.querySelector('[data-del-evt]');
    if (del) del.onclick = () => {
      daysData[dayIdx].timeline.splice(eidx, 1);
      saveData(tripDataRaw);
      renderItinerary(daysData);
      computeAndRenderTotals();
    };
  });
  
  document.querySelectorAll('[data-add-evt][data-day-idx]').forEach(btn => {
    const dayIdx = Number(btn.getAttribute('data-day-idx'));
    if (isNaN(dayIdx) || dayIdx < 0 || dayIdx >= daysData.length) return;
    btn.onclick = () => {
      daysData[dayIdx].timeline.push({time:'',title:'',note:''});
      saveData(tripDataRaw);
      renderItinerary(daysData);
      computeAndRenderTotals();
    };
  });
  
  document.querySelectorAll('input.photo-upload[type="file"][data-day-idx]').forEach(inp => {
    const dayIdx = Number(inp.getAttribute('data-day-idx'));
    if (isNaN(dayIdx) || dayIdx < 0 || dayIdx >= daysData.length) return;
    inp.onchange = (e) => {
      const file = inp.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        daysData[dayIdx].photo = reader.result;
        saveData(tripDataRaw);
        renderItinerary(daysData);
        computeAndRenderTotals();
      };
      reader.readAsDataURL(file);
    };
  });
  
  document.querySelectorAll('button.dev-photo-delete[data-day-idx]').forEach(btn => {
    if (btn.hasAttribute('data-day')) {
      const dayIdx = Number(btn.getAttribute('data-day-idx'));
      if (isNaN(dayIdx) || dayIdx < 0 || dayIdx >= daysData.length) return;
      btn.onclick = () => {
        delete daysData[dayIdx].photo;
        saveData(tripDataRaw);
        renderItinerary(daysData);
        computeAndRenderTotals();
      };
    }
  });
}
  </script>
</body>
</html>
