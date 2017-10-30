%include('header.tpl')
<h1>Resultado de Mongo</h1>
	%for i in cursor:
			<h3>{{i['available']}}
			{{i['warranty_years']}}
			{{i['name']}}
			{{i['price']}}
			{{i['_id']}}
			{{i['type']}}
			{{i['brand']}}</h3><br>
	%end
%include('footer.tpl')