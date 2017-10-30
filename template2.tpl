%include('header.tpl')
<h1>Resultado de Mongo</h1>
	% if col = "zip":
		for i in cursor:
			<h3>{{i["city"]}}	{{i["state"]}}	{{i["pop"]}}	{{i["loc"]}}</h3><br>
	%end
	% if col = "product":
		for i in cursor:
			{{i}}<br>
	%end
	
%include('footer.tpl')