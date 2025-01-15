import {SortingTable} from './sortTableClass.js'

main()


function main() {
    const table = document.getElementsByTagName('table')[0];
    const nameHeading = document.querySelector('#nameHeading');
    const workedTimeHeading = document.querySelector('#workedTimeHeading');

    const sorter = new SortingTable(table, '#name'); // Single instance
    let sorted = false; // Track sorting state

    nameHeading.addEventListener('click', () => {
        if (!sorted) {
            sorter.sortAlpha();
        } else {
            sorter.unsort();
        }
        sorted = !sorted;
    });

    workedTimeHeading.addEventListener('click', () => {
        if (!sorted) {
            sorter.sortTime();
        } else {
            sorter.unsort();
        }
        sorted = !sorted;
    });
}


