<!DOCTYPE>
<html>
	<head>
		<title> Nýskráning</title>
	</head>
	<body>
		<h1>Nýskráning</h1>
		<form action='/skra' method='post' accept-charset="ISO-8859-1">
			Tegund bíls: <br> <input type="text" name="tegund" required> <br>
			Skráningarnúmer bíls:<br><input type="text" name="skraningarnr" pattern="^\[A-Z]{2}-\d{3}$" placeholder="AA-111"  required> <br>
			Verksmiðjunúmer: <br> <input type="text" name="verksmidjunr" required> <br>
			Skráningardagur: <br> <input type="text" name="skraningardagur" required> <br>
			Næsta skoðun: <br> <input type="text" name="skodun" required> <br>
			CO2 Losun: <br> <input type="number" name="co2" required> <br>
			þyngd: <br> <input type="number" name="thyngd" required> <br>
			Staða:  <input type="radio" name="stada" value="i" checked> Í umferð<br>
  					<input type="radio" name="stada" value="ur"> Úr umferð<br>
			<input type="submit" name="Skrá">
			<p><a href="http://localhost:8080/leita">Hætta við og fara aftur í leit</a></p>

		</form>
	</body>
</html>