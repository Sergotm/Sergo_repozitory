'''UML-(Unified Modeling Language — уніфікована мова моделювання) — мова графічного опису для об'єктного моделювання в галузі розробки програмного забезпечення, 
для моделювання бізнес-процесів, системного проектування та відображення організаційних структур.
UML є мовою широкого профілю, це відкритий стандарт, що використовує графічні позначення для створення абстрактної моделі системи, 
яка називається UML-моделлю. UML була створена для визначення, візуалізації, проектування та документування, переважно, програмних систем. 
UML не є мовою програмування, але на основі UML-моделей можлива генерація коду.'''

# TODO Асоціація
# Коли один об'єкт використовує інший або залежить від нього, відношення називається асоціацією. В UML асоціація позначається простою стрілкою, яка спрямована у бік залежності

# TODO Композиція
# Це відношення «частина-ціле» між двома об'єктами, коли один з них включає в себе інший. 
# Особливість цього відношення полягає в тому, що компонент може існувати лише як частина контейнера. Місто складається з вулиць
# (Ромб направлений у бік контейнера, а стрілка — у бік об'єкта, що включається)

# TODO Агрегація
# Це менш суворий варіант композиції, коли один об'єкт просто має посилання на інший об'єкт. Тут контейнер не керує життєвим циклом компонента. 
# Компонент може існувати окремо від контейнера. Наприклад, школа має вчителів, але зв'язок тут слабший у порівнянні з містом-вулиця.
# В UML агрегація зображується як композиція, але з порожнім ромбом.
