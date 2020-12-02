''' Weapon Class
- To have a subclass for each weapon.
@author: Shaylen Mistry (unless stated otherwise)
'''
import pygame
from classes.spritesheet import SpriteSheet
# from spritesheet import SpriteSheet
# arms spirtesheets
BASIC_ARMS_LOCATION = 'graphics/spritesheets/basic-arms.png'
SWORD_ARMS_LOCATION = 'graphics/spritesheets/sword-arms.png'
BOOMERANG_ARMS_LOCATION = 'graphics/spritesheets/boomerang-arms.png'

#static images
SWORD_LOCATION = 'graphics/weapons/sword.png'
BOOMERANG_LOCATION = 'graphics/weapons/boomerang-static.png'

print()

class Weapon(pygame.sprite.Sprite):
    def __init__(self, owner, sprite_sheet_location):
        pygame.sprite.Sprite.__init__(self)
        self.owner = owner
        self.screen = owner.screen        
        self.owned = True

        # Loading Sprite Sheet
        image_types = owner.character_data['actions']
        image_directions = owner.character_data['directions']
        char_size = [32, 32]
        scaled_size = owner.scaled_size
        coords = owner.character_data
    
        self.loadSpriteSheets(image_types, image_directions, scaled_size,
                                char_size, coords, sprite_sheet_location)

        # Setting up initial image
        self.state = owner.state
        self.image = self.images[self.state[0]][self.state[1 ]]
        self.index = owner.image_index
        self.rect = self.image[self.index].get_rect()
        self.rect.centerx = self.owner.rect.centerx
        self.rect.centery = self.owner.rect.centery


    
    def loadSpriteSheets(self, image_types, image_directions, scaled_size, 
                        char_size, coords, sprite_sheet_location,
                        background_colour = (0, 255, 0)):
        ''' Assigns animation images to self


        '''
        self.spritesheet = SpriteSheet(sprite_sheet_location)
        self.images = {}
        for image_type in image_types:
            self.images[image_type] = {}
            for image_direction in image_directions:
                self.images[image_type][image_direction] = []
                for coord in coords[image_type][image_direction]:
                    specific_image = pygame.transform.scale(
                            self.spritesheet.image_at(coord, char_size),
                            scaled_size
                            )
                    specific_image.set_colorkey(background_colour)

                    self.images[image_type][image_direction] += [specific_image]

    def display(self):
        ''' display function

        state takes form [action, direction], images[action][direction] gives a list of images
        '''

        # Get owner variables
        x, y = self.owner.plot_rect.centerx, self.owner.plot_rect.centery
        self.state = self.owner.state
        self.index = self.owner.image_index
        action, direction = self.state[0], self.state[1]

        # Select Image
        self.image = self.images[action][direction]

        # Update rect position
        self.rect.center = x, y
        
        # Determines whether owner is alive 
        if not self.owner.alive
            self.owned = False

        # Rect position alive
        if self.owner.alive:
            x, y = self.owner.rect.centerx, self.owner.rect.centery
        if self.owner.alive:
            self.rect.center = x, y 
            
        # Blit to screen
        if self.owned:
            self.screen.blit(self.image[self.index], self.rect)
        else:
            self.screen.blit(self.weapon, self.rect)            
            
        # Update dropped weapon
        if owner.alive:
            self.rect_death = self.rect
            self.screen.blit(self.image[self.index], self.rect)

        if not self.owner.alive:
            self.owned = False
            self.rect_death.bottom = 100
            if self.owner.sate[0] != 'idle':
                if self.owner[1] == 'right':
                    self.rect.right -= 2
                if self.owner.state[1] == 'left':
                self.rect_death.right += 2
            self.screen.blit(self.weapon, self.rect_death)
        



class Sword(Weapon):
    sprite_sheet_location = SWORD_ARMS_LOCATION
    def __init__(self, owner):
        Weapon.__init__(self, owner, self.sprite_sheet_location)
    
    
    self.weapon = pygame.image.load(SWORD_LOCATION)

class Boomerang(Weapon):
    sprite_sheet_location = BOOMERANG_ARMS_LOCATION
    def __init__(self, owner):
        Weapon.__init__(self, owner, self.sprite_sheet_location)

    self.weapon = pygame.image.load(BOOMERANG_LOCATION)

class Arms(Weapon):
    sprite_sheet_location = BASIC_ARMS_LOCATION
    def __init__(self, owner):
        Weapon.__init__(self, owner, self.sprite_sheet_location)


    
