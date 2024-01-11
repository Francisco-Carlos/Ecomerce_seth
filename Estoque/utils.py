import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_pg = buffer.getvalue()
    graph = base64.b64encode(image_pg)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_estoq(x, y):
    cor = ['b', 'g', 'r']
    plt.switch_backend('AGG')
    plt.figure(figsize=(15, 9))
    plt.title('Produtos')
    p = plt.bar(x, y, color=cor)
    plt.bar_label(p)
    plt.xticks(rotation=90)
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_lucro(x, y):
    cor = ['b', 'g', 'r']
    plt.switch_backend('AGG')
    plt.figure(figsize=(15, 9))
    plt.title('Produtos')
    plt.bar(x, y, color=cor)
    # plt.bar_label(p)
    plt.xticks(rotation=0)
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.tight_layout()
    graph = get_graph()
    return graph
