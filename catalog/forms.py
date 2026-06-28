from django import forms

from .models import Product

forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "price", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Единый класс для всех полей
        for field in self.fields.values():
            if isinstance(
                field.widget, (forms.TextInput, forms.NumberInput, forms.EmailInput)
            ):
                field.widget.attrs["class"] = "form-control"
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["rows"] = 5
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = "form-select"
            elif isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs["class"] = "form-control"
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"

    def clean_name(self):
        """Валидация названия продукта"""
        name = self.cleaned_data.get("name")
        if name:
            name_lower = name.lower()
            for word in forbidden_words:
                if word in name_lower:
                    raise forms.ValidationError(
                        f'Название содержит запрещенное слово: "{word}". '
                        f"Пожалуйста, используйте другое название."
                    )
        return name

    def clean_description(self):
        """Валидация описания продукта"""
        description = self.cleaned_data.get("description")
        if description:
            description_lower = description.lower()
            found_words = []
            for word in forbidden_words:
                if word in description_lower:
                    found_words.append(word)

            if found_words:
                words_str = ", ".join(f'"{w}"' for w in found_words)
                raise forms.ValidationError(
                    f"Описание содержит запрещенные слова: {words_str}. "
                    f"Пожалуйста, удалите их из описания."
                )
        return description

    def clean_price(self):
        """Валидация цены продукта"""
        price = self.cleaned_data.get("price")

        if price is not None and price < 0:
            raise forms.ValidationError(
                "Цена не может быть отрицательной. Пожалуйста, введите корректную цену."
            )

        if price is not None and price == 0:
            raise forms.ValidationError(
                "Цена не может быть равна нулю. Пожалуйста, введите цену больше нуля."
            )

        return price


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "price", "category", "is_published"]
