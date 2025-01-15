export { SortingTable };

class SortingTable {
    static originalData = null;

    constructor(table, selector) {
        this.table = table;
        this.selector = selector;
        this.data = Array.from(this.table.getElementsByTagName('tbody')[0].children);

        // Initialize originalData only once
        if (!SortingTable.originalData) {
            SortingTable.originalData = this.data.map(row => row.cloneNode(true)); // Deep copy
        }
    }

    #removeBody() {
        const body = this.table.getElementsByTagName('tbody')[0];
        while (body.childElementCount) {
            body.removeChild(body.firstElementChild);
        }
    }

    #sortAlphaData() {
        this.data.sort((a, b) => {
            const elementA = a.querySelector(this.selector);
            const elementB = b.querySelector(this.selector);

            const nameA = elementA ? elementA.innerText : '';
            const nameB = elementB ? elementB.innerText : '';

            return nameA.localeCompare(nameB);
        });
        this.sortedData = this.data;
    }

    #sortTimeData() {
        const seconds = [];
        const newData = [];
        for (let i = 0; i < this.data.length; i++) {
            let wholeTime = this.data[i].querySelector('#workedTime')?.innerText ?? '';
            const splitTime = wholeTime.split(':');
            const totalSeconds =
                parseFloat(splitTime[0]) * 3600 +
                parseFloat(splitTime[1]) * 60 +
                parseFloat(splitTime[2]);
            seconds.push(totalSeconds);
            const objectData = {
                totalSeconds: totalSeconds,
                originalData: this.data[i]
            };
            newData.push(objectData);
        }
        newData.sort((a, b) => a.totalSeconds - b.totalSeconds);
        this.sortedTimeData = newData;
    }

    #rebuildAlphaBody() {
        const body = this.table.getElementsByTagName('tbody')[0];
        for (let i = 0; i < this.sortedData.length; i++) {
            body.appendChild(this.sortedData[i]);
        }
    }

    #rebuildOriginalBody() {
        const body = this.table.getElementsByTagName('tbody')[0];
        for (let i = 0; i < SortingTable.originalData.length; i++) {
            body.appendChild(SortingTable.originalData[i].cloneNode(true));
        }
    }

    #rebuildTimeBody() {
        const body = this.table.getElementsByTagName('tbody')[0];
        for (let i = 0; i < this.sortedTimeData.length; i++) {
            body.appendChild(this.sortedTimeData[i]['originalData']);
        }
    }

    sortAlpha() {
        this.#sortAlphaData();
        this.#removeBody();
        this.#rebuildAlphaBody();
    }

    sortTime() {
        this.#sortTimeData();
        this.#removeBody();
        this.#rebuildTimeBody();
    }

    unsort() {
        this.#removeBody();
        this.#rebuildOriginalBody();
    }
}


