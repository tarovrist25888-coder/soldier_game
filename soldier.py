import consts


def create_soldier():
    row=0
    col=0
    return row,col

def is_valid_position(row,col):
    if row<0:
        return False
    if col<0:
        return False
    if row+consts.SOLDIER_HEIGHT>consts.FIELD_ROWS:
        return False
    if col+consts.SOLDIER_WIDTH>consts.FIELD_COLS:
        return False
    return True
def move_soldier(row,col,direction):
    new_row=row
    new_col=col

    if direction=="up":
        new_row-=1
    elif direction=="down":
        new_row+=1
    elif direction=="left":
        new_col-=1
    elif direction=="right":
        new_col+=1
    if is_valid_position(new_row,new_col):
        row=new_row
        col=new_col
    return row,col

def create_soldier_body(row,col):
    body=[]
    for r in range(row,consts.SOLDIER_HEIGHT):
        for c in range(col,consts.SOLDIER_WIDTH):
            body.append((r,c))
    return body

def create_soldier_legs(row,col):
    legs=[]
    leg_row=row+consts.SOLDIER_HEIGHT-1
    for c in range(col,consts.SOLDIER_WIDTH):
        legs.append((leg_row,c))
    return legs
