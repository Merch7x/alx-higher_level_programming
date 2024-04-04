$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (greeting) {
      $('DIV#hello').text(greeting.hello);
    }

  });
});
