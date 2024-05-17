# python-scripts
### Helpful python scripts


# Disable Screen Lock

The `disable_screen_lock.py` will prevent the Windows screen lock during set hours. This is helpful if you are working from a private place and do not want to enter your password after leaving your computer, but do want it to resume screen locking at a certain point in the day.
It will also move the mouse curser 1 px and back every 100 seconds to keep your status "green".

```python
python disable_screen_lock.py
```
Current limitations:
- Not configured to differentiate work and non-work days.