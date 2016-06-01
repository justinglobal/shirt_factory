'use strict';

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
      success: function(data){
        var imgElement = $('<img>');
        imgElement.attr('src', 'data:image/png;base64,' + data)
        $('body').append(imgElement)
      }
  });
}
