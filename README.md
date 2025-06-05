# 🧮 Calculadora de Impuestos (Consola - Python)

## 📌 Descripción

La **Calculadora de Impuestos** es una aplicación de consola desarrollada en Python que permite calcular el monto total a pagar por un producto o servicio aplicando diferentes tipos de impuestos. Esta herramienta es especialmente útil para autónomos, pequeños negocios o cualquier persona que necesite calcular rápidamente el precio final con impuestos incluidos.

---

## 🎯 Objetivo

Desarrollar una solución simple, interactiva y confiable que:

- Calcule impuestos aplicando tasas predefinidas o personalizadas.
- Evite errores manuales comunes.
- Permita sumar múltiples tipos de impuestos a un solo producto o servicio.
- Ayude a entender cuánto se paga realmente por impuestos.

---

## 📋 Funcionalidades Principales

- **Menú Interactivo**: Con opciones claras para calcular impuestos, ver tipos de impuestos disponibles o salir del programa.
- **Ingreso del precio base**: El usuario ingresa el precio de un producto o servicio.
- **Selección de impuestos**:
  - IVA (10%)
  - Impuesto Especial (5%)
  - Impuesto Local (8%)
  - Otro (tasa personalizada)
- **Cálculo de impuestos múltiples**: Posibilidad de agregar más de un tipo de impuesto por producto.
- **Visualización de resultados detallados**: Se muestra el precio base, impuestos aplicados y total con impuestos.
- **Validación de entradas**: Se asegura que los valores ingresados sean válidos (números positivos).
- **(Opcional)**: Posibilidad de guardar los resultados en un archivo de texto o CSV.

---

## 🧪 Ejemplo de Uso

```text
---------------------------------------------------
             CÁLCULO DE IMPUESTOS
---------------------------------------------------
Ingrese el precio base del producto o servicio:
> 100

Seleccione el tipo de impuesto:
1. IVA (10%)
2. Impuesto Especial (5%)
3. Impuesto Local (8%)
4. Otro (personalizado)
> 1

¿Desea agregar otro impuesto?
1. Sí
2. No
> 2

---------------------------------------------------
           RESULTADO DEL CÁLCULO
---------------------------------------------------
Precio Base: $100.00
Impuesto(s):
- IVA (10%): $10.00
Total con impuestos: $110.00
