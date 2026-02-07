<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <link rel="icon" href="https://www.practicemock.com/static/images/favicon.ico"  type="image/x-icon"/>
  <title>Image Upload</title>
</head>
<style>
* {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
}
body {
  background-color: #f2f2f2;
}
.navbar {
  display: flex;
  background-color: #fff;
  height: 60px;
  margin-bottom: 20px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}
.navbar-header {
  width: 100%;
  display: flex;
  padding-inline: 30px;
  align-items: center;
  justify-content: space-between;
}
.header-images {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.container-body {
  width: max-content;
  margin: auto;
  padding-top: 30px;
}
article {
  display: flex;
  flex-direction: column;
  padding: 20px;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px;
}
.cbox {
  padding: 5px 15px;
  border-radius: 5px;
  margin-bottom: 10px;
}
.clabel {
  margin-bottom: 10px;
  font-weight: 600;
}
.btn-upload, .btn-submit {
  padding: 8px 34px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  outline: none;
  border: none;
}
.btn-submit {
  background-color: #304cb2;
  color: #fff;
}
#errorMessage {
  color: red;
  margin-top: 10px;
}
#output {
  margin-top: 10px;
}
</style>
<body>
  <div class="wrapper">
    <div class="container">
      <div class="navbar">
        <div class="navbar-header">
          <div class="header-images">
            <img src="https://u1.oliveboard.in/exams/img/logo/logo.png"> 
          </div>
          <p>Image Upload</p>
          <p>Thakshith</p>
        </div>
      </div>
      <div class="container-body">
        <article>
          <label for="imageInput" class="clabel">Upload PNG Image</label>
          <input type="file" id="imageInput" class="cbox" accept=".png">
          <div id="output">No file selected.</div>
          <div id="errorMessage"></div>
          <button class="btn-submit" id="captureFile">Submit</button>
        </article>
      </div>
    </div>
  </div>

  <script src="https://s3-ap-southeast-1.amazonaws.com/sg2.oliveboard.in/static/js/jquery.js"></script> 
  <script>
    $(document).ready(function () {
      let imageFile = null;

      $('#imageInput').on('change', function () {
        const fileInput = this;
        $('#output').text('No file selected.');
        $('#errorMessage').text('');

        if (fileInput.files.length === 0) return;

        const file = fileInput.files[0];
        const fileName = file.name.toLowerCase();

        // Validate file is a PNG
        if (!fileName.endsWith('.png')) {
          $('#errorMessage').text('Error: Only PNG files are allowed.');
          fileInput.value = '';
          imageFile = null;
          return;
        }

        // Optional: Check size (e.g., not empty)
        if (file.size === 0) {
          $('#errorMessage').text('Error: The selected file is empty.');
          fileInput.value = '';
          imageFile = null;
          return;
        }

        imageFile = file;
        $('#output').text(`Selected File: ${file.name}`);
      });

      $('#captureFile').click(function () {
        if (!imageFile) {
          alert('No file selected.');
          return;
        }

        var url = '/thakshith/templatetool1/py/imageupload.cgi';  // Your backend endpoint
        var formData = new FormData();
        formData.append('imageFile', imageFile);  // Match backend field name

        $.ajax({
          url: url,
          type: 'POST',
          data: formData,
          processData: false,
          contentType: false,
          dataType: 'json',
          success: function(response) {
            if (response.status === 'success') {
              alert('Success: ' + response.message);
            } else {
              alert('Fail: ' + (response.message || 'Unknown error'));
            }
          },
          error: function(xhr, status, error) {
            alert('An error occurred while uploading the file: ' + error);
          }
        });
      });
    });
  </script>
</body>
</html>
