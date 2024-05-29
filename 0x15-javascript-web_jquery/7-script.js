$(document).ready(function() {
    const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.get(apiUrl, (char) => {
        $('DIV#character').text(char.name);
    });
});