/*
 * exp_9_b.c
 *
 * Created: 27-10-2025 17:58:50
 *  Author: Douglas Aubre
 */ 

#include <avr/io.h>

void T1Delay();

int main(void)
{
	DDRB = (1 << 4);
	
	while(1)
	{
		T1Delay();
		PORTB |= (1 << 4);
		
		T1Delay();
		PORTB &= ~(1 << 4);
	}
}

void T1Delay()
{
	TCNT1H = 0x85;
	TCNT1L = 0xee;
	TCCR1A = 0;
	TCCR1B = 0x04; 
	
	while((TIFR & (1 << TOV1)) == 0);
	TCCR1A = 0;
	TCCR1B = 0;
	TIFR = 1;
}