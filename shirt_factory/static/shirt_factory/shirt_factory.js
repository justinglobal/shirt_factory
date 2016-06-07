'use strict';

/*
Makes encoded string of ascii art img file adds it as an <img> source url
and prepends the <img> to an html element via selector
*/
function submitImage() {
  var formData = new FormData();
  var imgInput = $('#input_img_file')[0].files[0];
  formData.append('input_img_file', imgInput);
  $.ajax({
    url: 'post/preview',
    data: formData,
    cache: false,
    contentType: false,
    processData: false,
    type: 'POST',
    success: function(data) {
      var imgElement = $('<img>');
      imgElement.attr('src', 'data:image/png;base64,' + data);
      $('#preview_area').prepend(imgElement);
    }
  });
}

/*
Sets id=preview to run submitImage on click and prevent default reload.
*/
function registerInitialEventHandlers() {
  $('#preview').on('click', function(event) {
    event.preventDefault();
    submitImage();
  });
}

$(document).ready(registerInitialEventHandlers);
