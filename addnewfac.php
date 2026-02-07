<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" href="https://www.practicemock.com/static/images/favicon.ico" type="image/x-icon" />
    <title>Faculty Name</title>
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
        width: 400px;
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

    .btn-upload,
    .btn-submit {
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
</style>

<body>
    <div class="wrapper">
        <div class="container">
            <div class="navbar">
                <div class="navbar-header">
                    <div class="header-images">
                        <img src="https://u1.oliveboard.in/exams/img/logo/logo.png">
                    </div>
                    <p>Faculty Name</p>
                    <p>Thakshith</p>
                </div>
            </div>
            <div class="container-body">
                <article>
                    <label for="nameInput" class="clabel">Enter Faculty Name</label>
                    <input type="text" id="nameInput" class="cbox" placeholder="Enter faculty name">
                    <label for="desc1Input" class="clabel">Enter Faculty Description</label>
                    <textarea id="desc1Input" class="cbox" placeholder="Enter faculty description"
                        rows="4"></textarea>

                    <div id="errorMessage"></div>
                    <button class="btn-submit" id="submitFaculty">Submit</button>
                </article>
            </div>
        </div>
    </div>

    <script src="https://s3-ap-southeast-1.amazonaws.com/sg2.oliveboard.in/static/js/jquery.js"></script>
    <script>


        $(document).ready(function () {
            $('#submitFaculty').click(function (e) {
                e.preventDefault();

                const name = $('#nameInput').val().trim();
                const desc1 = $('#desc1Input').val().trim();

                if (!name || !desc1) {
                    alert('Please fill in both fields.');
                    return;
                }

                $.ajax({
                    url: '/thakshith/templatetool1/py/facultyname.cgi',  // Adjust path as needed
                    type: 'POST',
                    data: {
                        name: name,
                        desc1: desc1
                    },
                    dataType: 'json',
                    success: function (response) {
                        if (response.status === 1) {
                            alert('Faculty added successfully! ID: ' + response.cid);
                        } else {
                            alert('Failed to add faculty.');
                        }
                    },
                    error: function (xhr, status, error) {
                        alert('An error occurred: ' + error);
                    }
                });
            });
        });
    </script>

</body>

</html>
