const container = document.querySelector('.container');
const seats = document.querySelectorAll('.row .seat:not(.occupied');
const total = document.getElementById('total');

const btnBuyTicket = document.getElementById('openFormBtn');

//скрипт для резервації
populateUI();
// loadOccupiedSeats();
let ticketPrice = 110;
let numbersOfSelectedSeats = [];
var actualSessionID;

// Seat click event
container.addEventListener('click', (e) => {
    if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
        e.target.classList.toggle('selected');

        updateSelectedCount();
    }
});

// update total and count
function updateSelectedCount() {
    const selectedSeats = document.querySelectorAll('.row .seat.selected');

    const selectedSeatsCount = selectedSeats.length;

    total.innerText = selectedSeatsCount * ticketPrice;
}

// get data from localstorage and populate ui
function populateUI() {
    const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));
    if (selectedSeats !== null && selectedSeats.length > 0) {
        seats.forEach((seat, index) => {
            if (selectedSeats.indexOf(index) > -1) {
                seat.classList.add('selected');
            }
        });
    }
}

function takeActualReservations(session_id) {
    $.ajax({
        url: '../../../../../reservation/',
        method: 'GET',
        data: {session_id: (session_id)},  // Provide the session ID
        success: function (response) {
            // Handle the successful response
            var placeNums = response.place_nums;
            console.log(placeNums);
        },
        error: function (xhr, status, error) {
            // Handle the error response
            console.log('Error:', error);
        }
    });
}

function takeReservationsReload(session_id) {
    $.ajax({
        url: '../../../../../reservation/',
        method: 'GET',
        data: {session_id: (session_id)},  // Provide the session ID
        success: function (response) {
            // Handle the successful response
            var placeNums = response.place_nums;
            var combined_string = placeNums.join(',');

// Разделение строки по запятой
            var split_list = combined_string.split(',');

// Преобразование в числа
            var result_place_nums = split_list.map(function (item) {
                return parseInt(item);
            });

            loadOccupiedSeats(result_place_nums);
        },
        error: function (xhr, status, error) {
            // Handle the error response
            console.log('Error:', error);
        }
    });
}

function loadOccupiedSeats(reservations) {

    let occupiedSeats = reservations;

    let allSeats = document.querySelectorAll('.row .seat');

    for (let i = 0, len = allSeats.length; i < len; i++) {
        allSeats[i].className = "seat";
    }
    for (let i = 0, len = occupiedSeats.length; i < len; i++) {
        allSeats[occupiedSeats[i] - 1].className = "seat occupied";
    }
}

btnBuyTicket.addEventListener('click', (e) => {
    let allSeats = document.querySelectorAll('.row .seat');

    for (let i = 0, len = allSeats.length; i < len; i++) {
        if (allSeats[i].className == 'seat selected') {
            numbersOfSelectedSeats.push(i + 1);
        }
    }
    console.log(numbersOfSelectedSeats);
});


// intial count and total
updateSelectedCount();