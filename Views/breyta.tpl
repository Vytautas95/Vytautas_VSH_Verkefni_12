<!DOCTYPE>
<html>
	<head>
		<title> Breyting</title>
	</head>
	<body>
		<h1>Breyta</h1>
		<form action='/breyting' method='post' accept-charset="ISO-8859-1">
			Tegund bíls: <br> <input type="text" name="tegund" Value={{tegund}} required> <br>
			Skráningarnúmer bíls:<br><input type="text" name="skraningarnr" pattern="^\[A-Z]{2}-\d{3}$" placeholder="AA-111"  Value={{skraningarnr}} required> <br>
			Verksmiðjunúmer: <br> <input type="text" name=verksmidjunr Value="{{verksmidjunr}}" required> <br>
			Skráningardagur: <br> <input type="text" name="skraningardagur" Value="{{skraningardagur}}" required> <br>
			Næsta skoðun: <br> <input type="text" name="skodun" Value={{skodun}} required> <br>
			CO2 Losun: <br> <input type="number" name="co2" Value={{co2}} required> <br>
			þyngd: <br> <input type="number" name="thyngd" Value={{thyngd}} required> <br>
			Staða:  <input type="radio" name="stada" value="í umferð" checked> Í umferð<br>
  					<input type="radio" name="stada" value="Úr umferð"> Úr umferð<br>
			<input type="submit" name="Skrá">
			<p><a href="http://localhost:8080/leita">Hætta við og fara aftur í leit</a></p>

		</form>
	</body>
</html>