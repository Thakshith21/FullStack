<?php
$result = exec("python2 py/drop.py");
list($outfacimg, $outlogo) = explode("|||", $result);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Templatetool</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="wrapper">
        <header class="main-header">
            <h1>Welcome to the Template Tool</h1>
        </header>

        <div class="content">
            <label for="templatecolor">Choose the Template</label>
                    <select name="#" id="templatecolor" required>
                        <option value="" disabled selected>Select a template</option>
                        <option value="blue" data-img="inputimg/social/social-blue.png">Template 1</option>
                        <option value="greenishyellow" data-img="inputimg/social/social-greenishyellow.png">Template 2</option>
                        <option value="lightblue" data-img="inputimg/social/social-lightblue.png">Template 3</option>
                        <option value="purple" data-img="inputimg/social/social-purple.png">Template 4</option>
                        <option value="yellow" data-img="inputimg/social/social-yellow.png">Template 5</option>
                    </select>
                    <div id="template-preview" class="preview">
                        <p>Template Preview:</p>
                        <img id="preview-image" src="" alt="Template Preview" class="imgpreview">
                    </div>
            <label for="logo">Select Logo:</label>
            <select name="#" id="logo" required>
                <option value="" disabled selected>Select a logo</option>
                <?php echo $outlogo; ?>
            </select>
            <div id="logo-preview" class="preview">
                            <p>Logo Preview:</p>
                            <img id="logo-image" src="" alt="Logo Preview" class="imgpreview">
                        </div>


            <label for="title">Title:</label>
            <input type="text" id="title" placeholder="Enter title here" required>

            <label for="subtitle">Sub Title:</label>
            <input type="text" id="subtitle" placeholder="Enter subtitle here" required>

            <label for="facimg1">Select Faculty1 Image:</label>
            <select name="#" id="facimg1" required>
                <option value="" disabled selected>Select a faculty image:</option>
                <?php echo $outfacimg; ?> 
            </select>
            <a href="http://dev.oliveboard.in/thakshith/templatetool1/imageupload.php" class="custom-link">Click here to add new image</a>
            <div id="facimg1-preview" class="preview">
                                        <p>Logo Preview:</p>
                                        <img id="facimg1-image" src="" alt="Faculty Preview" class="imgpreview">
                                    </div>

            <label for="facimg2">Select Faculty2 Image:</label>
            <select name="#" id="facimg2" required>
                <option value="" disabled selected>Select a faculty image</option>
                <?php echo $outfacimg; ?> 
                
            </select>
            <div id="facimg2-preview" class="preview">
                                                    <p>Logo Preview:</p>
                                                    <img id="facimg2-image" src="" alt="Faculty Preview" class="imgpreview">
                                                </div>


            <label for="facname1">Faculty 1 Name:</label>
            <input type="text" id="facname1" placeholder="Enter Faculty 1 Name" required>

            <a href="http://dev.oliveboard.in/thakshith/templatetool1/addnewfac.php" class="custom-link">Click here to add new Faculty</a>
            <label for="facname2">Faculty 2 Name:</label>
            <input type="text" id="facname2" placeholder="Enter Faculty 2 Name" required>

            <label for="facdesc1">Faculty 1 Description:</label>
            <input type="text" id="facdesc1" placeholder="Enter Faculty 1 Description" required></textarea>

            <label for="facdesc2">Faculty 2 Description:</label>
            <input type="text" id="facdesc2" placeholder="Enter Faculty 2 Description" required></textarea>

            <label for="date">Enter date:</label>
            <input type="date" id="date" required>

            <label for="time">Enter time:</label>
            <input type="time" id="time" required>

            <label for="venue">Enter Reg:</label>
            <input type="text" id="reg" placeholder="Register Now" value="Register Now" required>

            <button class="btn1">Submit</button>
        </div>
<div id="downloadLinks" style="display:none;">
    <p><a href="/thakshith/templatetool1/output/appbanner.png" download="appbanner.png">Click here to download App Banner</a></p>
    <p><a href="/thakshith/templatetool1/output/desktop.png" download="desktop.png">Click here to download Desktop Banner</a></p>
    <p><a href="/thakshith/templatetool1/output/push.png" download="push.png">Click here to download Push Notification Image</a></p>
    <p><a href="/thakshith/templatetool1/output/popup.png" download="popup.png">Click here to download Popup Image</a></p>
    <p><a href="/thakshith/templatetool1/output/social.png" download="social.png">Click here to download Social Media Image</a></p>
    <p><a href="/thakshith/templatetool1/output/ppt.png" download="ppt.png">Click here to download ppt Image</a></p>
</div>
    </div>


    <script src="https://practicemock.s3.ap-south-1.amazonaws.com/static/js/jquery.js"></script>
    <script>
$(document).ready(function(){
            // Template preview functionality
            $("#templatecolor").change(function () {
                var selectedOption = $(this).find("option:selected");
                var imgSrc = selectedOption.data("img");

                if (imgSrc) {
                    $("#preview-image").attr("src", imgSrc);
                    $("#template-preview").show();
                } else {
                    $("#template-preview").hide();
                }
            });
            // Logo preview functionality
            $("#logo").change(function () {
                var selectedOption = $(this).find("option:selected");
                var imgSrc = selectedOption.data("img");

                if (imgSrc) {
                    $("#logo-image").attr("src", imgSrc);
                    $("#logo-preview").show();
                } else {
                    $("#logo-preview").hide();
                }
            });

            // Faculty1 preview functionality
            $("#facimg1").change(function () {
                var selectedOption = $(this).find("option:selected");
                var imgSrc = selectedOption.data("img");

                if (imgSrc) {
                    $("#facimg1-image").attr("src", imgSrc);
                    $("#facimg1-preview").show();
                } else {
                    $("#facimg1-preview").hide();
                }
            });
            // Faculty2 preview functionality
            $("#facimg2").change(function () {
                var selectedOption = $(this).find("option:selected");
                var imgSrc = selectedOption.data("img");

                if (imgSrc) {
                    $("#facimg2-image").attr("src", imgSrc);
                    $("#facimg2-preview").show();
                } else {
                    $("#facimg2-preview").hide();
                }
            });
             // Faculty 1 auto-fill functionality
            $("#facimg1").change(function () {
                var selectedOption = $(this).find("option:selected");
                var name = selectedOption.data("name");
                var desc = selectedOption.data("desc");
                
                if (name) {
                    $("#facname1").val(name);
                    $("#facdesc1").val(desc);
                }
            });
            // Faculty 2 auto-fill functionality
            $("#facimg2").change(function () {
                var selectedOption = $(this).find("option:selected");
                var name = selectedOption.data("name");
                var desc = selectedOption.data("desc");
                
                if (name) {
                    $("#facname2").val(name);
                    $("#facdesc2").val(desc);
                }
            });
            
    $(".btn1").click(function(){
        var template = $('#templatecolor').val();
        var logo = $('#logo').val();
        var title = $('#title').val();
        var subtitle = $('#subtitle').val();
        var facimg1 = $("#facimg1").val();
        var facimg2 = $("#facimg2").val();
        var facname1 = $("#facname1").val();
        var facname2 = $("#facname2").val();
        var facdesc1 = $("#facdesc1").val();
        var facdesc2 = $("#facdesc2").val();
        var dateValue = $("#date").val();

        console.log(title);
            // Format date from YYYY-MM-DD to DD Month
            if (dateValue) {
                var date = new Date(dateValue);
                var day = date.getDate();
                var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
                var month = monthNames[date.getMonth()];
                dateValue = day + " " + month;
            }
        var timeValue = $("#time").val();
            // Format time to show hours with AM/PM
            if (timeValue) {
                var timeParts = timeValue.split(':');
                var hour = parseInt(timeParts[0]);
                var ampm = hour >= 12 ? 'PM' : 'AM';
                hour = hour % 12;
                hour = hour ? hour : 12; // Convert 0 to 12
                timeValue = hour + " " + ampm;
            }
        //var times = $("#time").val();
        var reg = $("#reg").val();

        var url = "py/2.py";

        var data = ({
            'template': template,
            'title': title,
            'subtitle': subtitle,
            'logo': logo,
            'facimg1': facimg1,
            'facimg2': facimg2,
            'facname1': facname1,
            'facname2': facname2,
            'facdesc1': facdesc1,
            'facdesc2': facdesc2,
            'dates': dateValue,
            'times': timeValue,
            'reg': reg
        });
        console.log(data);

        $.post(url, data, function(res){
            if (res.status == 1){
                alert("Images generated successfully!");
                $("#downloadLinks").slideDown(); // Show the download links div
            } else {
                alert("Image generation failed.");
                $("#downloadLinks").slideUp(); // Optionally hide if it was previously shown
            }
        }, 'json'); // Expect JSON response from 1.py
    });
});

    </script>

</body>

</html>
