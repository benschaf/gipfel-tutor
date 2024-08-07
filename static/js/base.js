$(document).ready(function () {
    $('.toast').toast('show')

    function updateCopyrightNotice() {
        let getYear = new Date().getFullYear()
        let yearID = $('#year')[0]
        if (getYear == 2024) {
            yearID.innerHTML = getYear
        } else {
            yearID.innerHTML = `2024 - ${getYear}`
        }
    }
    updateCopyrightNotice()
});