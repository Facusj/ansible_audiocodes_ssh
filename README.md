### NEED UPDATE ###


# telemetry
TICK stack for monitoring and telemetry collection

### Automation scripts

#### Crontab

Hay dos modalidades para la ejecucion de los playbooks de ansible. A través de un script loop.py que queda en ejecución constante y es el encargado de la iteración y, de forma alternativa, descansar en cron para la iteración a través de newcos-telemetry.py.

En ambos casos, los scripts python son llamados desde cron a través de un bash script llamado start.sh. En el primer escenario, ese script monitorea que loop.py se este ejecutando correctamente. En el segundo, llama a newcos-telemetry.py para la ejecución del playbook. La ejecución del playbook se realiza a través de python por los siguientes motivos:

- Procesos zombies de ansible se limpian antes de una nueva ejecución para evitar memory leaks
- Generación de logs a filesystem para troubleshooting
- Limpieza de logs
- Posible interacción con apis (telegram, influx) para generar reportes

Cron config:
```
# m h  dom mon dow   command
*/3 * * * * /code/newcos-telemetry/ansible/sbc/scripts/start.sh
0 0 */2 * * rm /code/newcos-telemetry/ansible/sbc/log/*.log 
```

#### telemetry
Script que consulta si se esta ejecutando un proceso con el script loop.py. Si se esta ejecutando no hará nada, si no se esta ejecutando iniciará la ejecución.

Se logueara la ejecución de este script en log/cron.log
