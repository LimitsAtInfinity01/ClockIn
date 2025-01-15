//TODO format dates to Month day, year.

// Function to format ISO strings to a readable format
const formatDateTime = (isoString) => {
    const date = new Date(isoString);
    return date.toLocaleString(); // Format to local date and time
};


// Function to format the workedTime duration
const formatWorkedTime = (duration) => {
    const regex = /P(\d+)DT(\d+)H(\d+)M([\d.]+)S/;
    const [, days, hours, minutes, seconds] = regex.exec(duration) || [];
    let readableTime = '';
    if (days > 0) readableTime += `${days} day${days > 1 ? 's' : ''}, `;
    if (hours > 0) readableTime += `${hours} hour${hours > 1 ? 's' : ''}, `;
    if (minutes > 0) readableTime += `${minutes} minute${minutes > 1 ? 's' : ''}, `;
    if (seconds) readableTime += `${parseFloat(seconds).toFixed(2)} seconds`;
    return readableTime.trim().replace(/,$/, ''); // Remove trailing comma
};

// Create a more readable object
const formattedData = (data) => {
    const object = {
        'first_name': data.first_name,
        'last_name':data.last_name,
        'timeIn': formatDateTime(data.timeIn),
        'timeOut': formatDateTime(data.timeOut),
        'worked_time': formatWorkedTime(data.workedTime)
    };
    return object;
};

// Correct Export
export { formattedData };
