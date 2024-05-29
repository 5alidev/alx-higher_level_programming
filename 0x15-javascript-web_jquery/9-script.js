$(document).ready(function() {
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.get(apiUrl, (data) => {
        $('DIV#hello').text(data.hello);
    });
});