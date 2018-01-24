#coding: utf-8
divisor=float(input("inserte aqui su divisor:"))
dividendo=float(input("inserte aqui su dividendo:"))
resultado= divisor%dividendo
if resultado == 12%2:
  print " es entero"
else:
  print " es una division decimal"
  print divisor/dividendo
