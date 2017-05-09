package rafaelmorales.practica.com.drive_calendar;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.TimePicker;

public class EventoCalendar extends AppCompatActivity {
    public static String fecha = Calendar.fecha, hora;
    Button seguir;
    TimePicker tp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_evento_calendar);

        tp = (TimePicker)findViewById(R.id.timePicker2);
        seguir = (Button)findViewById(R.id.btnNext);

        seguir.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                hora = tp.getCurrentHour() +":"+ tp.getCurrentMinute();
                Intent intent = new Intent(EventoCalendar.this, EventoCalendar.class);
                startActivity(intent);
            }
        });

    }
}
