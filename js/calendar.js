document.addEventListener('DOMContentLoaded', () => {
    const calendarElement = document.getElementById('calendar');
    const displayDate = document.getElementById('selectedDate');
    const monthYearDisplay = document.getElementById('monthYear');
    const prevMonthBtn = document.getElementById('prevMonth');
    const nextMonthBtn = document.getElementById('nextMonth');
    const now = new Date();
    const monthNames = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
    let selectedDate = null;
    let currentMonth = now.getMonth();
    let currentYear = now.getFullYear();
    let selectedDateValue = null;

    function createCalendar(year, month) {
        const firstDay = new Date(year, month, 1).getDay();
        const lastDate = new Date(year, month + 1, 0).getDate();

        let table = '<table><thead><tr>';
        table += '<tr><th>Пн</th><th>Вт</th><th>Ср</th><th>Чт</th><th>Пт</th><th>Сб</th><th>Вс</th></tr></thead><tbody><tr>';

        let dayOfWeek = firstDay === 0 ? 6 : firstDay - 1;
        for (let i = 0; i < dayOfWeek; i++) {
            table += '<td></td>';
        }

        for (let date = 1; date <= lastDate; date++) {
            const day = (dayOfWeek + date - 1) % 7;
            const dateValue = `${year}-${String(month + 1).padStart(2, '0')}-${String(date).padStart(2, '0')}`;
            table += `<td data-date="${dateValue}">${date}</td>`;
            if (day === 6 && date < lastDate) {
                table += '</tr><tr>';
            }
        }

        table += '</tr></tbody></table>';
        calendarElement.innerHTML = table;

        document.querySelectorAll('td[data-date]').forEach(td => {
            td.addEventListener('click', () => {
                if (selectedDate) {
                    selectedDate.classList.remove('selected');
                }
                selectedDate = td;
                selectedDate.classList.add('selected');
                selectedDateValue = td.dataset.date;
                displayDate.textContent = `Выбранная дата: ${selectedDateValue}`;
            });
        });

        monthYearDisplay.textContent = `${monthNames[month]} ${year}`;
    }

    function changeMonth(offset) {
        currentMonth += offset;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        } else if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        createCalendar(currentYear, currentMonth);
    }

    prevMonthBtn.addEventListener('click', () => changeMonth(-1));
    nextMonthBtn.addEventListener('click', () => changeMonth(1));

    createCalendar(currentYear, currentMonth);
});
