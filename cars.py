from jinja2 import Template

T1 = """Hello {{name}}"""

T2 = """Fuck you {{name}}"""

T3 = """

<!DOCTYPE html>
<head>
<h1> Jnanpith </h1>
<p> Bhartiya Jnanpith is a literary organisation based in Delhi. It also presents highest literacy awards in India. </p>
<link rel="stylesheet" href="style.css">
</head>
<body>
<h2> Awardees </h2>
<table style="border:1px solid black;">
<thead>
<tr style="background-color:lightgreen;">
<th>Year</th>
<th>Recipient(s)</th>
<th>Language(s)</th>
</tr>
</thead>
<tr><td>1965</td><td>G. Sankara Kurup</td><td>Malayalam</td></tr>
<tr><td>1966</td><td>Tarasankar Bandyopadhyay</td><td>Bengali</td></tr>
<tr><td>{{data["year"]}}</td><td>{{data["name"]}}</td><td>{{data["language"]}}</td></tr>
</table>

"""

data = {"year": 1956, "name": "Jai Shri Ram" , "language" : "Malyalam"}

def main():
    obj1 = Template(T1)
    obj2 = Template(T2)
    obj3 = Template(T3)
    print(obj1.render(name = "Haider"))
    print(obj2.render(name = "Faizal"))
    print(obj3.render(data = data))
                    
main()

if __name__ == "__main__":
    main()

