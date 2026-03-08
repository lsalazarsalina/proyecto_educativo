from __future__ import annotations
"""
core/services/minvu_pdf_filler.py
Rellena el Formulario 12.4 MINVU — Solicitud de Regularización Ley 20.898 Art. 3°
Superficie máxima: 140 m² | Avalúo máximo: 2.000 UF
"""
from dataclasses import dataclass, field
from pathlib import Path
from pypdf import PdfReader, PdfWriter


@dataclass
class DatosFormulario124:
    # ── ENCABEZADO ──────────────────────────────────────────────────────────
    municipalidad: str = ""
    numero_solicitud: str = ""
    fecha_ingreso: str = ""
    region: str = "Metropolitana"

    # ── SECCIÓN 1: DATOS DE LA PROPIEDAD ────────────────────────────────────
    calle_inmueble: str = ""
    numero_inmueble: str = ""
    rol_sii: str = ""
    manzana: str = ""
    lote_excel: str = ""
    loteo_localidad: str = ""
    plano_loteo: str = ""

    # ── SECCIÓN 2: DECLARACIÓN JURADA ───────────────────────────────────────
    declarante_nombre: str = ""
    declarante_ci: str = ""
    declarante_calle: str = ""
    declarante_numero: str = ""
    rol_avaluo: str = ""
    comuna_cbr: str = ""
    inscrito_fojas: str = ""
    inscrito_anio: str = ""
    inscrito_numero: str = ""
    conservador_bienes_raices: str = ""
    anio_inscripcion: str = ""
    registro_propiedad_anio: str = ""

    # ── SECCIÓN 3: DATOS DEL PROPIETARIO ────────────────────────────────────
    propietario_nombre: str = ""
    propietario_rut: str = ""
    propietario_rep_legal: str = ""
    propietario_rep_rut: str = ""
    propietario_calle: str = ""
    propietario_num: str = ""
    propietario_comuna: str = ""
    propietario_email: str = ""
    propietario_telefono: str = ""
    propietario_celular: str = ""
    propietario_empresa: str = ""
    propietario_empresa_rut: str = ""
    personeria_se_acredita: str = ""
    personeria_fecha: str = ""
    personeria_escritura_fecha: str = ""
    personeria_notario: str = ""
    personeria_otro: str = ""
    personeria_otro_fecha: str = ""

    # ── SECCIÓN 4: DATOS DEL ARQUITECTO ─────────────────────────────────────
    arq_empresa_nombre: str = ""
    arq_empresa_rut: str = ""
    arq_nombre: str = ""
    arq_rut: str = ""
    arq_profesion: str = "ARQUITECTO"
    arq_patente: str = ""
    arq_calle: str = ""
    arq_numero: str = ""
    arq_comuna: str = ""

    # ── SECCIÓN 5.1: LOCALIZACIÓN ───────────────────────────────────────────
    en_copropiedad: bool = False

    # ── SECCIÓN 5.2: PERMISOS ANTERIORES ────────────────────────────────────
    tiene_permiso_anterior: bool = False
    permiso_anterior_num: str = ""
    permiso_anterior_anio: str = ""
    tiene_recepcion_anterior: bool = False
    recepcion_anterior_num: str = ""
    recepcion_anterior_anio: str = ""

    # ── SECCIÓN 5.3: SUPERFICIES ─────────────────────────────────────────────
    sup_1p_con_permiso: str = ""
    sup_1p_regularizar: str = ""
    sup_1p_total: str = ""
    sup_2p_con_permiso: str = ""
    sup_2p_regularizar: str = ""
    sup_2p_total: str = ""
    sup_3p_con_permiso: str = ""
    sup_3p_regularizar: str = ""
    sup_3p_total: str = ""
    sup_total_con_permiso: str = ""
    sup_total_regularizar: str = ""
    sup_total_total: str = ""
    superficie_terreno_m2: str = ""

    # ── SECCIÓN 5.4: CARGA Y DENSIDAD ───────────────────────────────────────
    carga_ocupacion: str = ""
    densidad_ocupacion: str = ""

    # ── SECCIÓN 5.5: AVALÚO FISCAL ──────────────────────────────────────────
    avaluo_pesos: str = ""
    avaluo_uf: str = ""
    avaluo_terreno_uf: str = ""

    # ── SECCIÓN 5.6: TIPO AGRUPAMIENTO ──────────────────────────────────────
    tipo_agrupamiento: str = ""          # AISLADO / PAREADO / CONTINUO
    norma_complementaria: str = ""

    # ── SECCIÓN 5.7: NORMAS URBANÍSTICAS ────────────────────────────────────
    coef_constructibilidad_permitido: str = ""
    coef_constructibilidad_existente: str = ""
    coef_ocupacion_permitido: str = ""
    coef_ocupacion_existente: str = ""
    adosamiento_permitido: str = ""
    adosamiento_existente: str = ""
    uso_suelo_permitido: str = ""
    uso_suelo_existente: str = ""
    densidad_permitida: str = ""
    densidad_existente: str = ""
    distanciamiento_permitido: str = ""
    distanciamiento_existente: str = ""
    altura_cierros_existente: str = ""
    rasante_existente: str = ""
    sist_agrup_permitido: str = ""
    sist_agrup_existente: str = ""
    altura_max_permitida: str = ""

    # ── SECCIÓN 5.8: CLASIFICACIÓN ──────────────────────────────────────────
    clasificacion_1: str = ""
    clasificacion_1_m2: str = ""
    clasificacion_2: str = ""
    clasificacion_2_m2: str = ""

    # ── SECCIÓN 5.9: ART. 70 ────────────────────────────────────────────────
    forma_cumplimiento_art70: str = ""   # CESION / APORTE / OTRO
    art70_otro_especificar: str = ""

    # ── SECCIÓN 5.10: CÁLCULO CESIÓN ────────────────────────────────────────
    cesion_densidad_ocupacion: str = ""
    cesion_porcentaje: str = ""
    cesion_avaluo_terreno: str = ""
    cesion_porcentaje_b: str = ""
    cesion_aporte_dinero: str = ""

    # ── SECCIÓN 6: ANTECEDENTES (checkboxes) ────────────────────────────────
    adj_listado: bool = False
    adj_cert_avaluo_simple: bool = False
    adj_cert_avaluo_detallado: bool = False
    adj_patente: bool = False
    adj_antecedentes_anteriores: bool = False
    adj_acuerdo_copropiedad: bool = False
    adj_espec_tecnicas: bool = False
    adj_croquis: bool = False
    adj_planos: bool = False
    adj_informe_profesional: bool = False
    adj_formulario_ine: bool = False
    adj_calculo_estructural: bool = False

    # ── NOTA ─────────────────────────────────────────────────────────────────
    nota: str = ""

    # ── COMPROBANTE (pág 3) ──────────────────────────────────────────────────
    comprobante_municipalidad: str = ""
    comprobante_numero_solicitud: str = ""
    comprobante_fecha_ingreso: str = ""
    comprobante_calle: str = ""
    comprobante_numero: str = ""


# ── MAPEO field_id PDF → atributo DatosFormulario124 ─────────────────────────
# Página 1
TEXTO_MAP = {
    # Encabezado
    "Texto1":          "municipalidad",
    "Texto2":          "numero_solicitud",
    "Fecha4_af_date":  "fecha_ingreso",
    # Sección 1 - Propiedad
    "Texto5":          "calle_inmueble",
    "Texto6":          "numero_inmueble",
    "Texto7":          "rol_sii",
    "Texto8":          "manzana",
    "Texto9":          "lote_excel",
    "Texto10":         "loteo_localidad",
    "Texto11":         "plano_loteo",
    # Sección 2 - DJ
    "Texto12":         "declarante_nombre",
    "Texto13":         "declarante_ci",
    "Texto14":         "declarante_calle",
    "Texto15":         "declarante_numero",
    "Texto16":         "rol_avaluo",
    "Texto17":         "comuna_cbr",
    "Texto18":         "inscrito_fojas",
    "Texto19":         "inscrito_anio",
    "Texto20":         "inscrito_numero",
    "Texto21":         "conservador_bienes_raices",
    "Texto22":         "anio_inscripcion",
    "Texto23":         "registro_propiedad_anio",
    # Sección 3 - Propietario
    "Texto24":         "propietario_nombre",
    "Texto25":         "propietario_rut",
    "Texto26":         "propietario_rep_legal",
    "Texto27":         "propietario_rep_rut",
    "Texto28":         "propietario_calle",
    "Texto29":         "propietario_num",
    "Texto30":         "propietario_comuna",
    "Texto31":         "propietario_email",
    "Texto32":         "propietario_telefono",
    "Texto33":         "propietario_celular",
    "Fecha35_af_date": "personeria_fecha",
    "Texto34":         "personeria_se_acredita",
    "Fecha36_af_date": "personeria_escritura_fecha",
    "Texto37":         "personeria_notario",
    "Texto38":         "personeria_otro",
    "Texto39":         "personeria_otro_fecha",
    # Sección 4 - Arquitecto
    "Texto40":         "arq_empresa_nombre",
    "Texto41":         "arq_empresa_rut",
    "Texto43":         "arq_nombre",
    "Texto44":         "arq_rut",
    "Texto46":         "arq_profesion",
    "Texto47":         "arq_patente",
    "Texto48":         "arq_calle",
    "Texto49":         "arq_numero",
    "Texto50":         "arq_comuna",
    # Sección 5.2 - Permisos
    "Texto59":         "permiso_anterior_num",
    "Texto60":         "permiso_anterior_anio",
    "Texto61":         "recepcion_anterior_num",
    "Texto62":         "recepcion_anterior_anio",
    # Página 2 - Superficies
    "Texto63":         "sup_1p_con_permiso",
    "Texto64":         "sup_1p_regularizar",
    "Texto65":         "sup_1p_total",
    "Texto66":         "sup_2p_con_permiso",
    "Texto67":         "sup_2p_regularizar",
    "Texto68":         "sup_2p_total",
    "Texto69":         "sup_3p_con_permiso",
    "Texto70":         "sup_3p_regularizar",
    "Texto71":         "sup_3p_total",
    "Texto72":         "sup_total_con_permiso",
    "Texto73":         "sup_total_regularizar",
    "Texto74":         "sup_total_total",
    "Texto75":         "superficie_terreno_m2",
    # 5.4 Carga
    "Texto76":         "carga_ocupacion",
    "Texto77":         "densidad_ocupacion",
    # 5.5 Avalúo
    "Texto78":         "avaluo_pesos",
    "Texto79":         "avaluo_uf",
    "Texto92":         "avaluo_terreno_uf",
    # 5.7 Normas
    "Texto84":         "coef_constructibilidad_permitido",
    "Texto85":         "coef_constructibilidad_existente",
    "Texto86":         "densidad_permitida",
    "Texto87":         "densidad_existente",
    "Texto88":         "distanciamiento_permitido",
    "Texto89":         "distanciamiento_existente",
    "Texto90":         "altura_cierros_existente",
    "Texto91":         "rasante_existente",
    "Texto94":         "coef_ocupacion_permitido",
    "Texto95":         "coef_ocupacion_existente",
    "Texto96":         "adosamiento_permitido",
    "Texto97":         "adosamiento_existente",
    "Texto98":         "uso_suelo_permitido",
    "Texto99":         "uso_suelo_existente",
    "Texto100":        "sist_agrup_permitido",
    "Texto101":        "sist_agrup_existente",
    "Texto102":        "altura_max_permitida",
    # 5.8 Clasificación
    "Texto103":        "clasificacion_1",
    "Texto104":        "clasificacion_1_m2",
    "Texto105":        "clasificacion_2",
    "Texto106":        "clasificacion_2_m2",
    # 5.10 Cesión
    "Texto107":        "cesion_densidad_ocupacion",
    "Texto108":        "cesion_porcentaje",
    "Texto109":        "cesion_avaluo_terreno",
    "Texto110":        "cesion_porcentaje_b",
    "Texto111":        "cesion_aporte_dinero",
    "Texto112":        "art70_otro_especificar",
    "Texto113":        "nota",
    # Página 3 - Comprobante
    "Texto114":        "comprobante_municipalidad",
    "Texto115":        "comprobante_calle",
    "Texto117":        "comprobante_numero",
    "Fecha116_af_date":"comprobante_fecha_ingreso",
    "Texto130":        "comprobante_numero_solicitud",
    "Texto131":        "nota",
}

CHECKBOX_MAP = {
    # 5.1 Copropiedad
    "Check Box53":  ("en_copropiedad", True),
    "Check Box54":  ("en_copropiedad", False),
    # 5.2 Permisos
    "Check Box55":  ("tiene_permiso_anterior", True),
    "Check Box56":  ("tiene_permiso_anterior", False),
    "Check Box57":  ("tiene_recepcion_anterior", True),
    "Check Box58":  ("tiene_recepcion_anterior", False),
    # 5.6 Agrupamiento
    "Check Box80":  ("tipo_agrupamiento", "AISLADO"),
    "Check Box81":  ("tipo_agrupamiento", "PAREADO"),
    "Check Box82":  ("tipo_agrupamiento", "CONTINUO"),
    "Check Box83":  ("tipo_agrupamiento", "ADOSAMIENTO"),
    # 5.9 Art 70
    # Sección 6 - Antecedentes
    "Check Box118": ("adj_listado", True),
    "Check Box119": ("adj_cert_avaluo_simple", True),
    "Check Box120": ("adj_cert_avaluo_detallado", True),
    "Check Box121": ("adj_patente", True),
    "Check Box122": ("adj_antecedentes_anteriores", True),
    "Check Box123": ("adj_acuerdo_copropiedad", True),
    "Check Box124": ("adj_espec_tecnicas", True),
    "Check Box125": ("adj_croquis", True),
    "Check Box126": ("adj_planos", True),
    "Check Box127": ("adj_informe_profesional", True),
    "Check Box128": ("adj_formulario_ine", True),
    "Check Box129": ("adj_calculo_estructural", True),
}

REGION_MAP = {
    "Arica y Parinacota": "A",
    "Tarapacá": "T",
    "Antofagasta": "A",
    "Atacama": "A",
    "Coquimbo": "C",
    "Valparaíso": "V",
    "O'Higgins": "O",
    "Maule": "M",
    "Ñuble": "Ñ",
    "Biobío": "B",
    "La Araucanía": "L",
    "Los Ríos": "L",
    "Los Lagos": "L",
    "Aysén": "A",
    "Magallanes": "M",
    "Metropolitana": "M",
}


def rellenar_pdf_124(datos: DatosFormulario124, pdf_original, pdf_salida) -> Path:
    pdf_original = Path(pdf_original)
    pdf_salida = Path(pdf_salida)

    reader = PdfReader(str(pdf_original))
    writer = PdfWriter()
    writer.append(reader)

    field_values = {}

    # Campos de texto
    for field_id, attr in TEXTO_MAP.items():
        valor = getattr(datos, attr, "")
        field_values[field_id] = str(valor) if valor else ""

    # Dropdown región
    field_values["Dropdown3"] = REGION_MAP.get(datos.region, "M")

    # Checkboxes
    checked = "/Sí"
    unchecked = "/Off"
    for field_id, (attr, expected_val) in CHECKBOX_MAP.items():
        actual_val = getattr(datos, attr, None)
        if isinstance(expected_val, bool):
            field_values[field_id] = checked if actual_val == expected_val else unchecked
        else:
            # Para agrupamiento: marcar si coincide
            field_values[field_id] = checked if actual_val == expected_val else unchecked

    writer.update_page_form_field_values(None, field_values, auto_regenerate=False)

    pdf_salida.parent.mkdir(parents=True, exist_ok=True)
    with open(pdf_salida, "wb") as f:
        writer.write(f)

    return pdf_salida


# Alias para compatibilidad
DatosFormulario123 = DatosFormulario124
rellenar_pdf_123 = rellenar_pdf_124
