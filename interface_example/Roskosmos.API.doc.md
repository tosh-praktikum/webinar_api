# Общее назначение

Модуль Roskosmos позволяет запускать космические корабли в любые точки Вселенной прямо с вашего домашнего компьютера!

# Создание космического корабля

```
from roskosmos import Spaceship
apollo = Spaceship("Apollo 13")
```

# API

* `spaceship.setup(**settings)` - наделяет ваш космический корабль любыми дополнительными характеристиками
* `spaceship.launch()` - запускает космический корабль в космос