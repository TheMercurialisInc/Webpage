document.addEventListener("DOMContentLoaded", function() {
    var audioPlayer = document.getElementById("audioPlayer");
    audioPlayer.play().catch(function(error) {
        console.log("Autoplay failed:", error);
    });
});

function updateVeteranCounters() {
    document.querySelectorAll('.veteran-tenure.ticking').forEach(function(el) {
        var pastDays = parseInt(el.dataset.pastDays, 10);
        var stintStart = new Date(el.dataset.stintStart);
        var now = new Date();
        var currentDays = Math.floor((now - stintStart) / 86400000);
        var totalDays = pastDays + currentDays;
        var years = Math.floor(totalDays / 365.25);
        var remaining = totalDays - Math.floor(years * 365.25);
        var months = Math.floor(remaining / 30.44);
        el.textContent = years + ' yrs ' + months + ' mo';
    });
}
updateVeteranCounters();
setInterval(updateVeteranCounters, 60000);
