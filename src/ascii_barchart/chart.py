values = [
    ("A", 2.16),
    ("B", 4.33),
    ("C", 6.57),
    ("D", 8.71),
]

def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)

def render_bar_chart(values):
    # Maximum aus den Werten ermitteln, damit die Skalierung stimmt
    max_val = max(val for _, val in values)

    # ANSI-Farbcodes (Rot, Grün, Gelb, Cyan)
    colors = [
        "\033[91m",  # Rot
        "\033[92m",  # Grün
        "\033[93m",  # Gelb
        "\033[96m"   # Cyan
    ]
    reset = "\033[0m"

    for i, (label, val) in enumerate(values):
        length = scale_bar(val, max_val)
        color = colors[i % len(colors)]
        
        # Balken mit Block-Zeichen und ANSI-Farbe
        bar = color + "█" * length + reset
        print(f"{label}: {bar} ({val})")

render_bar_chart(values)