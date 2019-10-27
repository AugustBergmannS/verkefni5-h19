{% extends "base.html" %}


{% block innihald %}
    <a href="/karfa"><i class="fas fa-cart-arrow-down"></i>:{{ k }}</a>
    <ol>
        {% for vara in vorur %}
            {% set mynd = vara[3] %}
            <h3> {{ vara[1] }} </h3><li>
            <div>
                <p>
                    <a href="/ikorfu/{{ vara[0] }}" class="vara"><img src="{{ url_for('static',filename=mynd) }}" alt="{{vara[1]}}">  </a>
                </p>
                {{vara[2]}} kr.
            </div>
        {% endfor %}
    </ol>
{% endblock %}