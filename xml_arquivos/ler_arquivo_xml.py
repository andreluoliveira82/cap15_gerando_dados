import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path

caminho_arquivo = Path("E:/OneDrive/Documentos/Fernando XML/XML/xml teste 04/arquivos xml/31180110659892000190550010000007891004640326-nfe.xml")

# Create an ElementTree object from the XML file
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

# Initialize lists to store data
fields = []
values = []

# Iterate through the XML elements
for element in root.iter():
    # Extract the tag (field name) and text (field value)
    tag = element.tag
    text = element.text
    fields.append(tag)
    values.append(text)

# Create a DataFrame
data = {"Field": fields, "Value": values}
df = pd.DataFrame(data)

# Display the DataFrame (you can also save it to a CSV or Excel file)
# print(df)

# Salvando o df em csv
df.to_csv("xml_nfe_1.csv", index=False)

