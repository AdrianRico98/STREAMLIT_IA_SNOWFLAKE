# Streamlit + Snowflake Cortex AI

Repositorio de práctica para el reto [#30DaysOfAI](https://www.linkedin.com/company/streamlit/) de Streamlit, con un flujo CI/CD completo integrado.

## Qué incluye

- **Apps de Streamlit con Cortex AI**
- **GitHub Action** para despliegue automático en Snowflake.
- **Setup completo** de Git Integration en Snowflake.

## Flujo de trabajo

```
Local dev → Commit → Push to main → GitHub Action → Snowflake Git Fetch → App actualizada
```

## Configuración

1. **En Snowflake**: Ejecuta `setup.sql` para crear la integración Git, el repositorio y las apps.
2. **En GitHub**: Configura los secrets del repositorio:
   - `SNOWFLAKE_ACCOUNT`
   - `SNOWFLAKE_USER`
   - `SNOWFLAKE_PASSWORD`
   - `SNOWFLAKE_ROLE`
   - `SNOWFLAKE_WAREHOUSE`
   - `SNOWFLAKE_DATABASE`
   - `SNOWFLAKE_SCHEMA`

3. **Haz push** y la GitHub Action sincronizará automáticamente tu código con Snowflake.

## Recursos

- [30 Days of AI - Streamlit](https://30days.streamlit.app/)
- [Snowflake Cortex AI Docs](https://www.snowflake.com/en/product/features/cortex/)
- [Git Integration in Snowflake](https://docs.snowflake.com/en/developer-guide/git/git-overview)