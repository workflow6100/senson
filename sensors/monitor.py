import eventlet

from st2reactor.sensor.base import Sensor


class HelloSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(HelloSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        pass
    def get_credentials():
        credentials = ServicePrincipalCredentials(
                    client_id = '94c1d9ea-ffd1-4340-8f19-d3ad284805d8',
                    secret = 'uJUcbJbJjN3Y3TXYRR*6lUVuV/Z0Av@]',
                    tenant = 'd5656af4-b7b3-45b9-9346-fb0547921fb7'
                    )
        return credentials

    def run(self):
        while not self._stop:
            SUBSCRIPTION_ID = '2f50f202-0a84-4c8c-a929-fcc5a3174590'
            GROUP_NAME = 'OmkarVmPlzDoNotRemove'
            LOCATION = 'West US'
            VM_NAME = 'OmkarVmPlzDoNotRemoveThis'
            resource_id = (
              "subscriptions/{}/"
              "resourceGroups/{}/"
              "providers/Microsoft.Compute/virtualMachines/{}"
               ).format(SUBSCRIPTION_ID, GROUP_NAME, VM_NAME)
            credentials = get_credentials()
            client = MonitorManagementClient(
                 credentials,
                 SUBSCRIPTION_ID
                 )        
            m=[]
            today = datetime.datetime.now()-timedelta(hours=6)
            yesterday = today - datetime.timedelta(minutes=5)
            metrics_data = client.metrics.list(
                           resource_id,
                          timespan="{}/{}".format(yesterday, today),
                          interval='PT1M',
                          metricnames='Percentage CPU',
                          aggregation='Maximum'
                          )
            for item in metrics_data.value:
              for timeserie in item.timeseries:
                for data in timeserie.data:
                   x=data.maximum
                   m.append(x)
            sum=0
            for m1 in m:
              sum=sum+m1
            avg=sum/5              
            payload = {'average': avg}
            self.sensor_service.dispatch(trigger='hello_st2.event1', payload=payload)         
            eventlet.sleep(60)

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
