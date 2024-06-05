//JavaScript script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
  $("#btn_translate").click(function() {
    const languageCode = $("#language_code").val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.ajax({
      url: url,
      dataType: "json",
      success: function(data) {
        $("#hello").text(data.hello);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error("Error fetching translation:", textStatus, errorThrown);
        $("#hello").text("Error: Could not fetch translation.");
      }
    });
  });
});
