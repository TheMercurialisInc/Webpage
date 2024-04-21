document.addEventListener("DOMContentLoaded", function() {
    var audioPlayer = document.getElementById("audioPlayer");
    audioPlayer.play().catch(function(error) {
        console.log("Autoplay failed:", error);
    });
});
