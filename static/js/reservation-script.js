const container = document.querySelector('.container');
const seats = document.querySelectorAll('.row .seat:not(.occupied');
const total = document.getElementById('total');

//скрипт для резервації
populateUI();
loadOccupiedSeats();
let ticketPrice = 110;

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

function loadOccupiedSeats() {


    let occupiedSeats = reservations;
    
    let allSeats = document.querySelectorAll('.row .seat');

    for (let i = 0, len = allSeats.length; i < len; i++) {
        allSeats[i].className = "seat";
    }
    for (let i = 0, len = occupiedSeats.length; i < len; i++) {
        allSeats[occupiedSeats[i]].className = "seat occupied";
    }
}

// intial count and total
updateSelectedCount();