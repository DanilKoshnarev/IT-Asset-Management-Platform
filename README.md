# IT Asset Management Platform

## Описание
IT Asset Management Platform - это комплексная система для управления IT-активами, включающая модули для отслеживания оборудования, управления лицензиями, мониторинга использования ресурсов и планирования обновлений.

## Структура проекта
Проект разделен на несколько слоев для улучшения читаемости и поддерживаемости кода:

- **Domain**: Основная бизнес-логика и правила.
- **Application**: Интерфейсы, юзкейсы и реализации для работы с данными.
- **Infrastructure**: Реализация деталей инфраструктуры, таких как модели данных, контроллеры и утилиты.
- **Presentation**: Визуализация данных и взаимодействие с пользователем.

## Установка
1. Клонируйте репозиторий:
    ```bash
    git clone <URL репозитария>
    ```
2. Перейдите в каталог проекта:
    ```bash
    cd it_asset_management
    ```
3. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск
Для запуска проекта выполните команду:
```bash
python src/Application.py
```

## Структура каталогов
```plaintext
it_asset_management/
├── src/
│   ├── domain/
│   │   ├── entities/
│   │   │   ├── Asset.py
│   │   │   └── License.py
│   │   ├── repositories/
│   │   │   └── AssetRepository.py
│   │   ├── services/
│   │   │   └── AssetService.py
│   │   └── usecases/
│   │       └── ManageAsset.py
│   ├── infrastructure/
│   │   ├── models/
│   │   │   └── AssetModel.py
│   │   ├── controllers/
│   │   │   └── AssetController.py
│   ├── Application.py
└── README.md
```

## Описание компонентов
### Domain
- **Asset.py**: Класс сущности IT-актива.
- **License.py**: Класс сущности лицензии.
- **AssetRepository.py**: Интерфейс репозитория IT-активов.

### Application
- **ManageAsset.py**: Юзкейс для управления IT-активами.
- **AssetService.py**: Сервис для управления IT-активами.

### Infrastructure
- **AssetModel.py**: Модель данных IT-актива.
- **AssetController.py**: Контроллер для управления IT-активами.

### Presentation
- **DataView.py**: Представление для отображения IT-активов (если необходимо).

## Лицензия
Этот проект лицензирован под лицензией MIT. Для получения дополнительной информации см. файл LICENSE.
