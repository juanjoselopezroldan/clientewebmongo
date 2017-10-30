%include('header.tpl')
<br>
<br>
<div>
	<form action="/resultado" method="post" style="float: center">
		<label>Usuario MongoDB: </label>
		<input type="text" name="usuario" required/><br>
		<label>Clave :</label>
		<input type="password" name="clave" required/><br>
		<label> Nombre Colección: </label>
		<input type="text" name="coleccion" required/><br>
		<br><br><br>
		<input type="submit" value="Buscar">
	</form>
</div>
<br>
%include('footer.tpl')