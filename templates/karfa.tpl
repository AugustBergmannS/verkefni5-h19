{% extends "base.html" %}

{% block innihald %}
    
    {% if k == 0 %}
        <h2>Karfan er tóm...</h2>
    {% else %}
        <a href="/taema">Tæma körfu</a><br><br>
        {% for item in karfa %}
            <a href="/eyda/{{ item }}">{{ vorur[item][1]}}   {{ vorur[item][2]}}</a><br>
        {% endfor %}
        <p>Heildarverð: {{ heild }}</p>
        <a href='/karfa/kaupa'>Kaupa</a>
        <br><br>
    {% endif %}
    
{% endblock %}