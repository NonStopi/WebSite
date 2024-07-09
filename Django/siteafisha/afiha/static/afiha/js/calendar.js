const calendar = document.getElementById('calendar');
const monthElement = document.getElementById('month');
const yearElement = document.getElementById('year');
const prevMonthButton = document.getElementById('prevMonth');
const nextMonthButton = document.getElementById('nextMonth');
let date = new Date();
let selectedDate;

const daysOfWeek = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'];
const months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];

prevMonthButton.onclick = function() {
    date.setMonth(date.getMonth() - 1);
    monthElement.classList.add('hidden');
    yearElement.classList.add('hidden');
    calendar.classList.add('hidden');
    setTimeout(function() {
        createCalendar();
        monthElement.classList.remove('hidden');
        yearElement.classList.remove('hidden');
        calendar.classList.remove('hidden');
    }, 500);
};

nextMonthButton.onclick = function() {
    date.setMonth(date.getMonth() + 1);
    monthElement.classList.add('hidden');
    yearElement.classList.add('hidden');
    calendar.classList.add('hidden');
    setTimeout(function() {
        createCalendar();
        monthElement.classList.remove('hidden');
        yearElement.classList.remove('hidden');
        calendar.classList.remove('hidden');
    }, 500);
};

function createCalendar() {
    calendar.innerHTML = '';
    const month = date.getMonth();
    const year = date.getFullYear();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const daysInPrevMonth = new Date(year, month, 0).getDate();
    let firstDay = new Date(year, month, 1).getDay();
    firstDay = (firstDay === 0) ? 7 : firstDay; // Переводим воскресенье на 7-й день

    monthElement.textContent = `${months[month]}`;
    yearElement.textContent = `${year}`;

    let row = document.createElement('tr');
    for (let i = 0; i < 7; i++) {
        const cell = document.createElement('td');
        cell.textContent = daysOfWeek[i];
        cell.classList.add('days_of_week');
        if (i >= 5) {
            cell.classList.add('weekend');
        }
        row.appendChild(cell);
    }
    calendar.appendChild(row);

    row = document.createElement('tr');
    calendar.appendChild(row);

    for (let i = 1; i < firstDay; i++) {
        const cell = document.createElement('td');
        cell.textContent = daysInPrevMonth - firstDay + i + 1;
        cell.classList.add('prevMonth'); // Добавляем класс 'prevMonth' для чисел прошлого месяца
        row.appendChild(cell);
    }

    for (let i = 1; i <= daysInMonth; i++) {
        if ((i + firstDay - 2) % 7 === 0) {
            row = document.createElement('tr');
            calendar.appendChild(row);
        }
        const cell = document.createElement('td');
        cell.textContent = i;
        if ((i + firstDay - 2) % 7 >= 5) {
            cell.classList.add('weekend');
        }
        cell.onclick = function() {
            if (selectedDate) {
                selectedDate.classList.remove('selected');
            }
            cell.classList.add('selected');
            selectedDate = cell;
            const baseUrl = window.location.origin;
            const date = cell.textContent.padStart(2, '0');
            mon = (month+1).toString().padStart(2, '0');
            const path = (year >= 2000) && (year <= new Date().getFullYear()) ?  `${searchUrl}?date=${date}&month=${mon}&year=${year}` : "";
            const newUrl = baseUrl + path;
            window.location.href = newUrl;
            //console.log(`Выбранная дата: ${year}-${month + 1}-${cell.textContent}`);
        };
        row.appendChild(cell);
    }
}

createCalendar();