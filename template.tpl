%include('header.tpl')
<br>
<br>
<div>
	<form action="/resultado" method="post" style="float: center">
		<label>Sitio (Ej. "Sevilla", "C/Oripo"):</label>
		<input type="text" name="sitio" required/><br>
		<label>Tipo (Ej. "Restaurante", "Estadios", "Cines"):</label>
		<input type="text" name="lugar" required/><br>
		<br><br><br>
		<input type="submit" value="Buscar">
	</form>

</div>
<br>
%include('footer.tpl')