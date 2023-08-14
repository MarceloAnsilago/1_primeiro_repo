bbas3_price = 4759  # Valor em centavos (47.59 * 100)
b3sa3_price = 1402  # Valor em centavos (14.02 * 100)
lot_size = 100
budget = 1000000  # Valor em centavos (R$10,000 * 100)

best_profit = 0
best_combination = None

for bbas3_qty in range(0, budget // bbas3_price + 1):
    b3sa3_qty = min(budget // b3sa3_price, bbas3_qty * lot_size)
    
    total_cost = bbas3_qty * bbas3_price + b3sa3_qty * b3sa3_price
    
    if total_cost <= budget:
        total_profit = b3sa3_qty * (bbas3_price - b3sa3_price)
        if total_profit > best_profit:
            best_profit = total_profit
            best_combination = (bbas3_qty, b3sa3_qty)

if best_combination:
    bbas3_qty, b3sa3_qty = best_combination
    print(f"Melhor combinação: Comprar {bbas3_qty} BBAS3 e vender {b3sa3_qty} B3SA3")
    print(f"Lucro estimado: R${best_profit / 100:.2f}")  # Convertendo de centavos para reais
else:
    print("Nenhuma combinação encontrada dentro do limite de orçamento.")


