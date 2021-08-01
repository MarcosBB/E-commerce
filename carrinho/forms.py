from django import forms

class AdicionarProdutoAoCarrinhoForm(forms.Form):
    quantidade = forms.TypedChoiceField(
        label="", choices=[(i,str(i)) for i in range(1, 21)], coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )