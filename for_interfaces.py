html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>jekyll ui</title>
</head>
<body>
<h2>emoji language gitcoin bounty</h2>
<p>Please enter the emoji code here: </p>
<input type="button" value="&#x1F41B" id="button1"/>
<input type="button" value="&#x1F31F" id="button2"/>
<input type="button" value="&#x1F477" id="button3"/>
<input type="button" value="&#x1F3C3" id="button4"/>
<form method="POST">
    <input name="text" type="text" value="" id="text" autocomplete="off" style="width: 300px; height: 150px" />
    <input type="submit">
</form>


<script type="text/javascript">
document.getElementById("button1").addEventListener('click', function () {
    var text = document.getElementById('text');
    text.value += ' &#x1F41B';
});
</script>
<script type="text/javascript">
document.getElementById("button2").addEventListener('click', function () {
    var text = document.getElementById('text');
    text.value += ' &#x1F31F';
});
</script>
<script type="text/javascript">
document.getElementById("button3").addEventListener('click', function () {
    var text = document.getElementById('text');
    text.value += ' &#x1F477';
});
</script>
<script type="text/javascript">
document.getElementById("button4").addEventListener('click', function () {
    var text = document.getElementById('text');
    text.value += ' &#x1F3C3';
});
</script>

</body>
</html>
"""