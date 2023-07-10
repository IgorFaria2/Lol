$(document).ready(function() {
    $("form").submit(function(event) {
        event.preventDefault();  // Prevent default form submission behavior

        // Get summoner name from the input field
        var summonerName = $("input[name='summoner_name']").val();
        
        // Send an AJAX request to the backend
        $.ajax({
            type: "POST",
            url: "/",
            data: { summoner_name: summonerName },
            success: function(response) {
                // Update the history container with the received JSON
                console.log(response["info"]["participants"][0]["summonername"])
                $("#historyContainer").text(JSON.stringify(response));
            }
        });
    });
});
