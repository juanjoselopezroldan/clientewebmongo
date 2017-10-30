%include('header.tpl')
<h3>Resultado de Mongo</h3>
	%for i in cursor:
			<h4>{{i}}</h4><br>
	%end
%include('footer.tpl')