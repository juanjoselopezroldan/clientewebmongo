%include('header.tpl')
<br>
<br>
<div>
	<form action="/map" method="post" style="float: left">
		<label>Sitio (Ej. "Sevilla", "C/Oripo"):</label>
		<input type="text" name="sitio" required/><br>
		<label>Tipo (Ej. "Restaurante", "Estadios", "Cines"):</label>
		<input type="text" name="lugar" required/><br>
		<label> Radio (Ind. en Kms):</label>
		<input type="number" value="1" min='1' name="radio" required/><br>
		<br><br><br>
		<input type="submit" value="Buscar">
	</form>

</div>
<br>
%include('footer.tpl')