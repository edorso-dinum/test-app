class DatabaseRouter:
    """
    Routes each app to the database that hosts its table:
    - `roles` app -> `premier_roles` database (`role_names` table).
    - `doublures` app -> `doublures` database (`doublure_names` table).
    """

    route_app_labels = {
        "roles": "premier_roles",
        "doublures": "doublures",
    }

    def db_for_read(self, model, **hints):
        return self.route_app_labels.get(model._meta.app_label)

    def db_for_write(self, model, **hints):
        return self.route_app_labels.get(model._meta.app_label)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return self.route_app_labels[app_label] == db
        return db == "default"
